from django.shortcuts import render
from .models import Employee, Device
from .serializers import (
    EmployeeSerializer,
    DeviceSerializer,
    EmployeeHistorySerializer,
    DeviceHistorySerializer,
)
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Model
from django.http import JsonResponse


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

    # def history(self):
    #     return Device.history.all()

    # def list(self, request, *args, **kwargs):
    #     queryset = Device.objects.values("name").distinct()
    #     print("ress", queryset)
    #     serializer = DeviceSerializer(queryset, many=True)

    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     # queryset = his.objects.all()
    #     data = request.data
    #     serializer = DeviceSerializer(data=data)
    #     serializer2 = HistorySerializer(data=data)
    #     if serializer.is_valid() and serializer2.is_valid():
    #         serializer.save()
    #         serializer2.save()

    # serializer = DeviceSerializer(queryset, many=True, context={"request": request})

    # serializer_context = {
    #     "request": request,
    # }
    # return Response()

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer_class(data=data)
    #     return super().create(request, *args, **kwargs)


class DeviceHistoryModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Device.history.all()
    serializer_class = DeviceHistorySerializer
    filterset_fields = "__all__"

    def devicehistory(request, pk):
        abc = Device.history.filter(id=pk)  # use filter instead of get
        # print("abc", abc)
        serializer = DeviceHistorySerializer(
            abc, many="True", context={"request": request}
        )
        return JsonResponse(serializer.data, safe=False)


class EmployeeHistoryModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.history.all()
    serializer_class = EmployeeHistorySerializer
    filterset_fields = "__all__"


# by setting many=True you tell drf that queryset contains mutiple items (a list of items)
# so drf needs to serialize each item with serializer class (and serializer.data will be a list)

# he JSON Response in Django set save=True by default, and the safe parameter as a data influencer
# makes JSON accept the Python Data-Type {Dictionaries} and nothing less.

# make it to safe=False for non dict type data
