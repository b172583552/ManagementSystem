from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

# Create your models here.
class Department(models.Model):
    title = models.CharField(verbose_name="title", max_length=32)

class UserInfo(models.Model):
    name = models.CharField(verbose_name="name", max_length=16)
    password = models.CharField(verbose_name="password", max_length=64)
    age = models.IntegerField(verbose_name="age")
    account_balance = models.DecimalField(verbose_name="account balance", max_digits=10, decimal_places=2, default=0)

    create_time = models.CharField(verbose_name="create_time", max_length=16)

    department = models.ForeignKey(to="Department", to_field="id", on_delete=models.SET_NULL, blank=True, null=True)
    #on_delete=models.CASCADE: delete all linked entity
    gender_choices = (
        (1, "male"),
        (2, "female"),
    )
    gender = models.SmallIntegerField(verbose_name="gender", choices=gender_choices)

