
DJANGO_APPS: list[str] = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS: list[str] = [
    'exercise',
    'judge',
    'submission',
    'language',
    'rank',
    'user'
]


EXTERNAL_APPS: list[str] = [
    'rest_framework',
    'rest_framework_simplejwt',
]


APPS: list[str] = DJANGO_APPS + PROJECT_APPS + EXTERNAL_APPS 

