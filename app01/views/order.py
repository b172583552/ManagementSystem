from datetime import datetime
import random

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django import forms
from app01 import models


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = models.Order
        exclude = ["order_id", "admin"]


def order_list(request):
    form = OrderModelForm()
    queryset = models.Order.objects.all().order_by("-id")
    no_of_items = 5
    page_object = Paginator(queryset, no_of_items)
    page_number = request.GET.get("page", "1")
    page = page_object.get_page(page_number)
    queryset = page

    return render(request, "order_list.html", {"queryset": queryset, "form": form})


def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.order_id = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        form.instance.admin_id = request.session["info"].get("admin_id")
        form.save()
        return redirect("/order/list/")
    else:
        return JsonResponse({"status": False, "error": form.errors})


def order_edit(request, nid):
    if request.method == "POST":
        row_object = models.Order.objects.get(id=nid)
        form = OrderModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/order/list/")




def order_delete(request, nid):
    models.Order.objects.filter(id=nid).delete()
    return redirect("/order/list/")


