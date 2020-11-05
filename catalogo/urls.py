from django.conf import settings
from catalogo.views import LibroDetailView
from django.urls.conf import path
from django.urls import re_path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.index, name="index"), # función url -> re_path
    re_path(r'^libros/$', views.LibroListView.as_view(), name='libros'),
    re_path(r'^libros/(?P<pk>\d+)$', views.LibroDetailView.as_view(), name='libro-detail')
]


