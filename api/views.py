from django.shortcuts import render
from .models import Employee, Device, History
from .serializers import EmployeeSerializer, DeviceSerializer, HistorySerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


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

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer_class(data=data)
    #     return super().create(request, *args, **kwargs)


class HistoryModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
