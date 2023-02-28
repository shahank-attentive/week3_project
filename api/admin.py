from django.contrib import admin

# Register your models here.
from .models import Employee, Device


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "employee_id", "email_id"]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "model"]


# @admin.register(History)
# class DeviceHistoryAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "user", "timestamp"]

# def current_user_name(self, instance):
#     return instance.current_user.name
