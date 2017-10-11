from django.conf.urls import url

from . import views

app_name = 'overseer'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process/$', views.process, name='process'),
    url(r'^(?P<avaliation_id>[0-9]+)/result/$', views.result, name='result'),
]
