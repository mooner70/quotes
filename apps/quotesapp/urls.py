from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^quotes$', views.quotes),
    url(r'^login$', views.login),
    url(r'^users$', views.user_registration),
    url(r'^logout$', views.logout),
    # url(r'^add$', views.add_quote),
    url(r'^add_fav$', views.add_fav),
    # url(r'^user_quotes/$', views.user_quotes),
    url(r'^user_quotes/(?P<id>\d+)$', views.user_quotes),
    url(r'^add_to_favorite/(?P<id>\d+)$', views.add_to_favorite),
    url(r'^remove_from_favorite/(?P<id>\d+)$', views.remove_from_favorite)
  ]