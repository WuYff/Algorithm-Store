from django.conf.urls import url

from . import views

app_name = 'astor_sys'

urlpatterns = [
    url(r'^$', views.index, name="index"),
]
