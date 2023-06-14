from django.shortcuts import render, redirect
from app01 import models
from django import forms
from django.core.paginator import Paginator

def department_list(request):
    queryset = models.Department.objects.all()
    page_object = Paginator(queryset, 1)
    page_number = request.GET.get("page", "1")
    page = page_object.get_page(page_number)
    queryset = page

    return render(request, "department_list.html", {"queryset": queryset})


def department_add(request):
    if request.method == "GET":
        attributes = models.Department.objects.all()[0].__dict__
        dict = {}
        for index, attribute in enumerate(attributes):
            if index > 1:
                dict[attribute] = attributes[attribute]
        print(dict)
        return render(request, "change.html",
                      {"name": "department", "attributes": dict})

    title = request.POST.get("title")

    models.Department.objects.create(title=title)

    return redirect("/department/list/")


def department_delete(request):
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()

    return redirect("/department/list/")


def department_edit(request, nid):
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        print(row_object.id, row_object.title)
        return render(request, "department_edit.html", {"row_object": row_object})

    else:
        title = request.POST.get("title")
        models.Department.objects.filter(id=nid).update(title=title)
        return redirect("/department/list")