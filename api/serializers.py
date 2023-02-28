from rest_framework import serializers
from .models import Employee, Device


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "name", "employee_id", "email_id"]


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    # h_serializer = HistorySerializer(many=True)

    class Meta:
        model = Device
        fields = ["id", "name", "model", "current_user"]


class EmployeeHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee.history.model
        fields = "__all__"
        write_only_feilds = ()


class DeviceHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device.history.model
        fields = "__all__"
        # read_only_fields = ["id", "name", "employee_id", "email_id"]
