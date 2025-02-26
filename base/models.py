from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=50)
    basic_salary = models.DecimalField(max_digits=13 ,decimal_places=0)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.title)


class Employee(models.Model):
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    national_id = models.CharField(max_length=16)
    birth = models.DateField(null=True)
    phone = models.CharField(max_length=16)
    address = models.TextField(null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
        
