from django.shortcuts import render, redirect
from app01 import models
def registration(request):
    if request.method == "GET":
        return render(request, "registration.html", {"error": ""})

    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not models.Admin.objects.filter(username=username).exists():
            models.Admin.objects.create(username=username, password=password)
        else:
            return render(request, "registration.html", {"error": "Username exists. Please use another username."})

        return redirect("/login")