from django.db.models import signals
from django.contrib.contenttypes.models import ContentType

from easymarkup.cache import set_to_cache
from easymarkup import conf


def field_to_cache(sender, **kwargs):
    '''
    Save rendered fields to cache for models and their fields
    spec in conf setting CTS_CACHE_ON_SAVE
    '''
    ct = ContentType.objects.get_for_model(sender)
    instance = kwargs['instance']
    for field in conf.CTS_CACHE_ON_SAVE['%s.%s' % ct.natural_key()]:
        for safe_mode in conf.CACHE_AUTO_FOR_SAFE_MODES:
            set_to_cache(instance, field, safe_mode=safe_mode)


for item in conf.CTS_CACHE_ON_SAVE.items():
    ct, fileds = item
    model = ContentType.objects.get_by_natural_key(**ct.split(".")).model_class()
    signals.post_save.connect(field_to_cache, sender=model)
