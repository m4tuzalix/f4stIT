from django.urls import path
from .views import *

urlpatterns=[
    path("", main, name="main"),
    path("search/", Search.as_view(), name="search"),
    path("about/", about, name="about")
]