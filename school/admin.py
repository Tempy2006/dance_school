from django.contrib import admin
from .models import Classroom, Course, DayOfTheWeek

admin.site.register(DayOfTheWeek)
admin.site.register(Classroom)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("subject", "day_of_the_week", "starting_hour", "classroom", "school")
    list_filter = ("day_of_the_week", "school")
    search_fields = ("subject",)
