from django.shortcuts import render
from .models import Issue

def home (request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})
def about (request):
    return render(request, 'itreporting/about.html', {'title': 'about'})
def contact (request):
    return render(request, 'itreporting/contact.html', {'title': 'contact'})
def report (request):
    return render(request, 'itreporting/report.html', {'title': 'report'})
