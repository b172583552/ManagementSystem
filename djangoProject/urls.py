"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01.views import department, user, admin, account, order

urlpatterns = [
    # path('admin/', admin.site.urls),

    #for Department
    path("department/list/", department.department_list),
    path("department/add/", department.department_add),
    path("department/delete/", department.department_delete),
    path("department/<int:nid>/edit/", department.department_edit),

    #for User
    path("user/list/", user.user_list),
    path("user/add/", user.user_add),
    path("user/<int:nid>/edit/", user.user_edit),
    path("user/<int:nid>/delete/", user.user_delete),

    #for admin
    path("admin/list/", admin.admin_list),
    path("admin/add/", admin.admin_add),
    path("admin/<int:nid>/edit/", admin.admin_edit),
    path("admin/<int:nid>/delete/", admin.admin_delete),

    path("login/", account.login),
    path("logout/", account.logout),
    path("captcha/", account.captcha),

    path("order/list/", order.order_list),
    path("order/add/", order.order_add),

]
