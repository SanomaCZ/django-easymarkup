import markdown2
from hashlib import md5

from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType

from django.utils.encoding import force_unicode, smart_str
from django.conf import settings

from easymarkup import conf


def normalize_key(key):
    if settings.DEBUG and len(key) < 250:
        return key
    return md5(key).hexdigest()


def get_cache_key(obj, field, **kwargs):
    if not conf.CACHE_FIELDS:
        return None
    start = "MARKDOWN_FIELD"
    ct = ContentType.objects.get_for_model(obj)
    natural_key = '%s-%s' % ct.natural_key()

    return normalize_key(':'.join((
                start,
                natural_key,
                str(obj.pk),
                str(field),
                ','.join(':'.join((key, smart_str(kwargs[key]))) for key in sorted(kwargs.keys()))
    )))


def markdown(obj, field, **kwargs):
    return markdown2.markdown(force_unicode(getattr(obj, field)),
                              extras=conf.MARKDOWN_EXTRAS,
                              safe_mode=kwargs.get('safe_mode', None))


def get_from_cache(obj, field, **kwargs):
    key = get_cache_key(obj, field, **kwargs)
    if key is None:
        return markdown(obj, field, **kwargs)
    result = cache.get(key)
    if result is None:
        result = set_to_cache(obj, field, **kwargs)
    return result


def set_to_cache(obj, field, **kwargs):
    key = get_cache_key(obj, field, **kwargs)
    value = markdown(obj, field, **kwargs)
    if key is not None:
        cache.set(key, value, timeout=conf.FIELD_CACHE_TIMEOUT)
    return value
