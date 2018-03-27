from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^quotes$', views.quotes),
    url(r'^login$', views.login),
    url(r'^registration$', views.user_registration),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add_quote),
    url(r'^add_fav$', views.add_fav),
  ]