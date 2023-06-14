from django.shortcuts import render, redirect
from app01 import models
from django import forms
from django.core.paginator import Paginator


class AdminModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ["username", "password"]


def admin_list(request):
    queryset = models.Admin.objects.all()
    page_object = Paginator(queryset, 1)
    page_number = request.GET.get("page", "1")
    page = page_object.get_page(page_number)
    queryset = page

    return render(request, "admin_list.html", {"queryset": queryset})


def admin_add(request):
    if request.method == "GET":
        # dict = {}
        #
        # attributes = models.Admin.objects.all().first().__dict__
        # for index, attribute in enumerate(attributes):
        #     if index > 1:
        #         dict[attribute] = attributes[attribute]
        # print(dict)
        # return render(request, "change.html",
        #               {"name": "admin", "attributes": dict})
        return render(request, "admin_add.html")

    else:
        form = AdminModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admin/list")

def admin_edit(request,nid):
    if request.method == "GET":


        attributes = models.Admin.objects.all()[0].__dict__
        dict = {}
        for index, attribute in enumerate(attributes):
            if index > 1:
                dict[attribute] = attributes[attribute]
        print(dict)
        return render(request, "change.html",
                      {"name": "admin", "attributes": dict})
    if request.method == "POST":
        row_query = models.Admin.objects.filter(id=nid).first()
        form = AdminModelForm(data=request.POST, instance=row_query)
        if form.is_valid():
            form.save()
            return redirect("/admin/list/")

def admin_delete(request, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/")