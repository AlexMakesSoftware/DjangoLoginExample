# Customisation of user login specific settings.

SITE_ID = 1
#TODO: for now, let's just send us home when we login.
LOGIN_REDIRECT_URL = '/' 
#Custom user model
#See: https://django-allauth.readthedocs.io/en/latest/account/advanced.html#custom-user-models
AUTH_USER_MODEL = 'customise_login.CustomUser'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None


AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
)