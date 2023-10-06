# Customisation of user login specific settings.

print("loading custom config now")

SITE_ID = 1
#TODO: for now, let's just send us home when we login.
LOGIN_REDIRECT_URL = '/' 
#Custom user model
AUTH_USER_MODEL = 'customise_login.CustomUser'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_USER_MODEL_USERNAME_FIELD = None


# ACCOUNT_USER_MODEL_USERNAME_FILED = None

# ACCOUNT_FORMS = {
#     'signup': 'customise_login.forms.CustomSignupForm',
# }

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
)