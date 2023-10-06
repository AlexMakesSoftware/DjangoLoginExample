
from django.urls import path
from .views import *

#Note: we're not declaring our own namespace here, we're overriding 'accounts', from the allauth package.

urlpatterns = [
    path('accounts/profile', ProfileView.as_view(), 'profile')
]
