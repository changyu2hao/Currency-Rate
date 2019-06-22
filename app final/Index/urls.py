from django.conf.urls import url
from . import  views


urlpatterns = [
    url(r'^get_trans/', views.get_trans),
]