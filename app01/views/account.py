from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01 import models
from django import forms
from django.core.paginator import Paginator


class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password


def login(request):

    if request.method == "GET":
        return render(request, "login.html", {"error": ""})

    else:
        print(request.POST)
        form = LoginForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
            if not admin_object:
                return render(request, "login.html", {"error": "Wrong Username or Password!"})
            else:
                request.session["info"] = admin_object.username
                return redirect("/admin/list/")

        else:
            return HttpResponse("false")


