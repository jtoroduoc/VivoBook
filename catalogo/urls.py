from django.urls.conf import path
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name="index") # función url -> re_path
]
