from django.urls import path

from catalog.views import home
from catalog.views import contacts

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
