from django.views.generic import DetailView, ListView
from .models import School


class SchoolListView(ListView):
    model = School


class SchoolDetailView(DetailView):
    model = School
