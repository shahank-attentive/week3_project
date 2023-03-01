from rest_framework import serializers
from .models import Employee, Device, History


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "name", "employee_id", "email_id"]


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    current_user = EmployeeSerializer(many=False)

    class Meta:
        model = Device
        fields = ["id", "name", "model", "current_user"]

    # def create(self, validated_data):
    #     data = validated_data.get("current_user")
    #     print(data)
    #     serializer = DeviceSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()

    #     return Device.objects.create(**validated_data)


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ["id", "emp", "dev", "time"]


# class EmployeeHistorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Employee.history.model
#         fields = "__all__"
#         write_only_feilds = ()


# class DeviceHistorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Device.history.model
#         fields = "__all__"
#         # read_only_fields = ["id", "name", "employee_id", "email_id"]
