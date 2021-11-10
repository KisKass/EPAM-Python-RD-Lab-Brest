from django.db import models


class Departments(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Department_name = models.CharField(max_length=30)


class Employees(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    employee_name = models.CharField(max_length=70)
    date_of_birth = models.DateField()
    department = models.ForeignKey('Departments', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
