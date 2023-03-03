from rest_framework import serializers
from .models import Employee, Device, Status, History


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "name", "employee_id", "email_id"]


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    current_user = EmployeeSerializer(many=True)

    class Meta:
        model = Device
        fields = ["id", "name", "model", "current_user"]

    def create(self, validated_data):
        data = validated_data.pop("current_user")
        print("data", type(data))  # data is list of dict
        print("to print", data)
        device = Device.objects.create(**validated_data)
        for a in data:  # fetching the list
            Employee.objects.create(device=device, **a)
        return device


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    # emp= EmployeeSerializer(many=True)
    # dev=DeviceSerializer()
    class Meta:
        model = History
        fields = ["id", "emp", "dev", "time"]


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    # history2 = HistorySerializer2()

    class Meta:
        model = Status
        fields = ["id", "emp", "dev", "time"]

    def create(self, validated_data):
        # a = Employee.objects.get(id=1)
        # if validated_data["emp"] == None:
        # validated_data["emp"]=a
        print("vaildated _data", validated_data)  # dict type
        data = validated_data
        print("to print", data)  # queryset
        his = Status.objects.create(**validated_data)
        History.objects.create(**data)
        return his

    # def create(self, validated_data):
    #     data = validated_data.pop("emp")
    #     print("to print", data)
    #     device = History.objects.create(**validated_data)
    #     for a in data:
    #         Employee.objects.create(device=device, **a)
    #     return device


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
