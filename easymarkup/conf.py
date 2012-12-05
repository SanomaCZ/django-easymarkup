from django.conf import settings

# set False if you do not use cache for fields that use markdown
CACHE_FIELDS = getattr(settings, 'EASYMARKUP_CACHE_FIELDS', True)

# TIMEOUT for caching rendered content of fields
FIELD_CACHE_TIMEOUT = getattr(settings, 'EASYMARKUP_FIELD_CACHE_TIMEOUT', 3 * 60 * 60)

# set python-markdown extras to be used for markdown call
MARKDOWN_EXTRAS = getattr(settings, 'EASYMARKUP_MARKDOWN_EXTRAS', [])

# specify content types natural keys as key and wanted fields as list value
# for on save cache rendered fileds
CTS_CACHE_ON_SAVE = getattr(settings, 'EASYMARKUP_CTS_CACHE_ON_SAVE', {})

# specify python-markdown safe_modes to be cached on save, chaoices are (True), (False) or (True, False)
CACHE_AUTO_FOR_SAFE_MODES = getattr(settings, 'EASYMARKUP_CACHE_AUTO_FOR_SAFE_MODES', (True))
