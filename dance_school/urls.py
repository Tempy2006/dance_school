from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("test/", views.test_view, name="test"),
    path("about/", views.about, name="about"),
    path("sedi/", include("schoolmanagement.urls")),
    path("scuola/", include("school.urls")),
    path("admin/", admin.site.urls),
]
