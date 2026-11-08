from django.http import HttpResponse
from django.shortcuts import render


def test_view(request):
    return HttpResponse("View di prova con HttpResponse")


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
