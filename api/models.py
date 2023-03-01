from django.db import models
from django.utils import timezone

# from simple_history.models import HistoricalRecords


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    employee_id = models.IntegerField()
    email_id = models.CharField(max_length=60)
    # history = HistoricalRecords()

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    current_user = models.ManyToManyField(Employee, through="History")
    # history = HistoricalRecords()

    def __str__(self):
        return self.name


class History(models.Model):
    dev = models.ForeignKey(Device, on_delete=models.CASCADE)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    time = models.DateTimeField()


# def __str__(self):
#     return self.name


# class Change(models.Model):
#     emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     changed_field = models.CharField("field_name", max_length=200)
#     changed_data = (
#         models.TextField()
#     )  # you can improve this by storing the data in compressed format
#     chaged_at = models.DateTimeField(default=timezone.now)
#     status = models.CharField(max_length=10, default="pending")
