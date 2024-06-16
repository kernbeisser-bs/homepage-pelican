AUTHOR = 'Kernbeißer Verbraucher-Erzeuger-Genossenschaft eG'
SITENAME = 'Kernbeißer'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

PAGES_SORT_ATTRIBUTE = 'sortorder'

# Blog
INDEX_SAVE_AS = 'blog.html'

# Theme
THEME = './themes/kernbeisser-bootstrap'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
    'i18n_subsites',
    'better_figures_and_images'
]
I18N_TEMPLATES_LANG = 'de'
SITELOGO = 'theme/img/kerni.svg'
SITELOGO_SIZE = '50px'
CC_LICENSE = 'CC-BY-SA'
RESPONSIVE_IMAGES = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Config
OPENING_HOURS = (
    ("Montag", "Geschlossen"),
    ("Dienstag", "Geschlossen"),
    ("Mittwoch", "16:00 - 18:30 Uhr"),
    ("Donnerstag", "17:00 - 19:30 Uhr"),
    ("Freitag", "16:00 - 18:30 Uhr"),
    ("Samstag", "11:30 - 14:00 Uhr"),
    ("Sonntag", "Geschlossen"),
)
SIDEBAR_IMAGES = (

)
LINKS = (
    ('Kernbeißer Cloud', 'https://cloud.kernbeisser.de'),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True