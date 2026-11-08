from django.urls import path
from . import views

app_name = "school"
urlpatterns = [
    path("dayoftheweek/", views.DayOfTheWeekListView.as_view(), name="dayoftheweek_list"),
    path("dayoftheweek/<int:pk>/", views.DayOfTheWeekDetailView.as_view(), name="dayoftheweek_detail"),
    path("classroom/", views.ClassroomListView.as_view(), name="classroom_list"),
    path("classroom/<int:pk>/", views.ClassroomDetailView.as_view(), name="classroom_detail"),
    path("course/", views.CourseListView.as_view(), name="course_list"),
    path("course/<int:pk>/", views.CourseDetailView.as_view(), name="course_detail"),
]
