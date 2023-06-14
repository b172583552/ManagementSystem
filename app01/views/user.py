from django.shortcuts import render, redirect
from app01 import models
from django import forms
from django.core.paginator import Paginator


def user_list(request):
    queryset = models.UserInfo.objects.all()
    page_object = Paginator(queryset, 1)
    page_number = request.GET.get("page", "1")
    page = page_object.get_page(page_number)
    queryset = page

    return render(request, "user_list.html", {"queryset": queryset})


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account_balance", "create_time", "gender", "department"]


def user_add(request):
    if request.method == "GET":
        context = {
            "gender_choices": models.UserInfo.gender_choices,
            "department_list": models.Department.objects.all()
        }
        return render(request, "user_add.html", context)

    if request.method == "POST":
        # get information required to update
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

        else:
            print("error")

        # models.UserInfo.objects.create(name=name, password=password, age=age,
        #                               account_balance=account, create_time=employment_time, gender=gender,
        #                               department_id=department_id)

        return redirect("/user/list")


def user_edit(request, nid):
    if request.method == "GET":
        context = {
            "gender_choices": models.UserInfo.gender_choices,
            "department_list": models.Department.objects.all(),
            "row_set": models.UserInfo.objects.get(id=nid)
        }
        return render(request, "user_edit.html", context)

    if request.method == "POST":
        row_object = models.UserInfo.objects.get(id=nid)
        form = UserModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/user/list/")


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
