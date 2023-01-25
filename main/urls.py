from django.urls import path 
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
]