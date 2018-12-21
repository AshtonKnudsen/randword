from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
        "word" : get_random_string(length=14)
        }
    if not "count" in request.session:
        request.session["count"] = 0
    if "count" in request.session:
        request.session["count"] += 1
    return render(request,"gen/index.html", context)
# Create your views here.
