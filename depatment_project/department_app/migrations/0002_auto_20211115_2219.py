# Generated by Django 3.2.9 on 2021-11-15 22:19

from django.db import migrations


def create_test_data(apps, schema_editor):
    Department = apps.get_model('department_app', 'Department')
    Department.objects.bulk_create([
        Department(Department_name='Commercial department'),
        Department(Department_name='HR department'),
        Department(Department_name='Financial department'),
        Department(Department_name='Administrative department')
    ])

    Employee = apps.get_model('department_app', 'Employee')
    Employee.objects.bulk_create([
        Employee(employee_name='Carol Young',
                 date_of_birth='1992-7-30',
                 department=Department.objects.get(Department_name='Commercial department'),
                 salary=123.45
                 ),
        Employee(employee_name='Nancy Rogers',
                 date_of_birth='2002-5-25',
                 department=Department.objects.get(Department_name='Commercial department'),
                 salary=1100.00,
                 ),
        Employee(employee_name='Patrick Miller',
                 date_of_birth='2001-3-7',
                 department=Department.objects.get(Department_name='HR department'),
                 salary=5555.01
                 ),
        Employee(employee_name='Howard Campbell',
                 date_of_birth='1980-11-22',
                 department=Department.objects.get(Department_name='Financial department'),
                 salary=111.00
                 ),
        Employee(employee_name='Gerald Long',
                 date_of_birth='1977-9-8',
                 department=Department.objects.get(Department_name='Administrative department'),
                 salary=423.41
                 ),
    ])


def delete_test_data(apps, schema_editor):
    Department = apps.get_model('department_app', 'Department')
    Department.objects.filter(Department_name='Commercial department').delete()
    Department.objects.filter(Department_name='HR department').delete()
    Department.objects.filter(Department_name='Financial department').delete()
    Department.objects.filter(Department_name='Administrative department').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_test_data, delete_test_data)
    ]