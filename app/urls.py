from django.conf.urls import url

from app import views

viewpatterns = [
    url(r'^$', views.frontpage_view, name='frontpage')
]

urlpatterns = viewpatterns