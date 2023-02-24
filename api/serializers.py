from rest_framework import serializers
from .models import Employee, Device, History


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "name", "employee_id", "email_id"]


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ["id", "d_name"]
        read_only_fields = ["id", "d_name"]


class DeviceSerializer(serializers.ModelSerializer):
    # h_serializer = HistorySerializer(many=True)

    class Meta:
        model = Device
        fields = ["id", "name", "model", "current_user"]

    # def create(self, validated_data):
    #     albums_data = validated_data.pop("h_serializer")
    #     musician = Device.objects.create(**validated_data)
    #     for album_data in albums_data:
    #         Album.objects.create(**album_data)
    #     return musician


# class HistorySerializer(serializers.ModelSerializer):


#     class Meta:
#         model = History
#         fields = ["id", "d_name"]
#         read_only_fields = ["id", "d_name"]
