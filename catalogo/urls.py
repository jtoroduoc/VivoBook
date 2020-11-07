from django.conf import settings
from django.urls.conf import path
from django.urls import re_path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.index, name="index"), # función url -> re_path
    re_path(r'^libros/$', views.LibroListView.as_view(), name='libros'),
    re_path(r'^libros/(?P<pk>\d+)$', views.LibroDetailView.as_view(), name='libro-detail'),
    re_path(r'^autores/$', views.AutorListView.as_view(), name='autores'),
    re_path(r'^autores/(?P<pk>\d+)$', views.AutorDetailView.as_view(), name='autor-detail'),
]


