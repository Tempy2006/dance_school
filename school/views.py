from django.views.generic import DetailView, ListView
from .models import DayOfTheWeek, Classroom, Course


class DayOfTheWeekListView(ListView):
    model = DayOfTheWeek


class DayOfTheWeekDetailView(DetailView):
    model = DayOfTheWeek


class ClassroomListView(ListView):
    model = Classroom


class ClassroomDetailView(DetailView):
    model = Classroom


class CourseListView(ListView):
    model = Course
    queryset = Course.objects.select_related("day_of_the_week", "classroom", "school")


class CourseDetailView(DetailView):
    model = Course
