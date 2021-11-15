from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Department_name = models.CharField(max_length=30, null=False, unique=True)

    class Meta:
        db_table = 'departments'
        verbose_name = 'Department name'


class Employee(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    employee_name = models.CharField(max_length=70, null=False)
    date_of_birth = models.DateField(null=False)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        db_table = 'employees'
        verbose_name = 'Employee name'
