from django.urls import path
from . import views

app_name = "schoolmanagement"
urlpatterns = [
    path("", views.SchoolListView.as_view(), name="school_list"),
    path("<int:pk>/", views.SchoolDetailView.as_view(), name="school_detail"),
]
