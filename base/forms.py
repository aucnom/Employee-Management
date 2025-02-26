from dataclasses import field
from django.forms import ModelForm
from .models import Job, Employee

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'