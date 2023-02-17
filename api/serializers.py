from rest_framework import serializers
from .models import Employee, Device


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "name", "employee_id", "email_id"]


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["id", "name", "model", "current_user"]


# class ChangeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Change
#         fields = ("project", "changed_field")
