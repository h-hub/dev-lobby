from django.shortcuts import render
import datetime

def index(request):
    today = datetime.datetime.now().date()
    return render(request, "home.html", {"today" : today})