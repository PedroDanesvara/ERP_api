from django.urls.resolvers import URLPattern
from companies.views.employees import Employees, EmployeeDetail
from companies.views.permissions import PermissionDetail
from django.urls import path

urlpatterns: list[URLPattern] = [
    path("employees", Employees.as_view()),
    path("employees/<int:employee_id>", EmployeeDetail.as_view()),
    path("permissions", PermissionDetail.as_view()),
]
