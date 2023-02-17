from django.shortcuts import render
from .models import Employee, Device
from .serializers import EmployeeSerializer, DeviceSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter


# Create your views here.
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ["name", "employee_id", "email_id"]


class DeviceModelViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = (SearchFilter,)
    search_fields = [
        "name",
        "=model",
        "current_user__name",
    ]  # Here we want exact match for model so '='
