from django.shortcuts import render, redirect
import datetime


def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')

    today = datetime.datetime.now().date()
    return render(request, "home.html", {"today": today})
