from datetime import datetime
from random import random

from django.http import JsonResponse
from django.shortcuts import render
from django import forms
from app01 import models
class OrderModelForm(forms.ModelForm):
    class Meta:
        model = models.Order
        exclude = ["order_id", "admin"]

def order_list(request):
    form = OrderModelForm()
    print(form)
    return render(request, "order_list.html", {"form": form})

def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.order_id = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        form.instance.admin_id = request.session["info"].get("admin_id")
        form.save()
        return JsonResponse({"status": True})
    else:
        return JsonResponse({"status": False, "error": form.errors})



