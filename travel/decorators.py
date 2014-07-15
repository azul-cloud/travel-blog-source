#import urlparse
#from functools import wraps
#from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
#from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from tbsdev.settings import ALT_LOGIN_URL
from social_auth.exceptions import AuthException

def social_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    try:
        actual_decorator = user_passes_test(
            lambda u: u.is_authenticated(),
            login_url=login_url,
            redirect_field_name=redirect_field_name
        )
        if function:
            return actual_decorator(function)
    except (AuthException):
        actual_decorator = user_passes_test(
            lambda u: u.is_authenticated(),
            login_url=ALT_LOGIN_URL,
            redirect_field_name=redirect_field_name
        )
        if function:
            return actual_decorator(function)
    return actual_decorator