from django.urls import path 
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.fp, name="front page"),
    path("home/", views.summary.as_view(), name="summary"),
    path("home2/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("apply/<int:id>", views.apply, name="apply"),
    path("create/application", views.CreateApplication.as_view(), name="Create Application"),
    path("create/course", views.CreateCourse.as_view(), name="Create Course"),
]