from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from schoolmanagement.models import School


class DayOfTheWeek(models.Model):
    number = models.PositiveSmallIntegerField("numero", unique=True, validators=[MinValueValidator(1), MaxValueValidator(7)])
    name = models.CharField("nome", max_length=15)

    class Meta:
        ordering = ["number"]
        verbose_name = "giorno della settimana"
        verbose_name_plural = "giorni della settimana"

    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField("nome", max_length=80)
    capacity = models.PositiveSmallIntegerField("capienza", validators=[MinValueValidator(1)])

    class Meta:
        ordering = ["name"]
        verbose_name = "aula"
        verbose_name_plural = "aule"

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.CharField("materia", max_length=100)
    day_of_the_week = models.ForeignKey(DayOfTheWeek, on_delete=models.PROTECT, verbose_name="giorno")
    starting_hour = models.TimeField("ora di inizio")
    classroom = models.ForeignKey(Classroom, on_delete=models.PROTECT, verbose_name="aula")
    school = models.ForeignKey(School, on_delete=models.PROTECT, verbose_name="sede")

    class Meta:
        ordering = ["day_of_the_week__number", "starting_hour"]
        verbose_name = "corso"
        verbose_name_plural = "corsi"

    def __str__(self):
        return self.subject
