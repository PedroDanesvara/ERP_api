from django.db import models


class Enterprise(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=175)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)


class TaskStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=155)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = "companies_task_status"


class Task(models.Model):
    title = models.TextField()
    description = models.TextField(null=True)
    due_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
