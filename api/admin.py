from django.contrib import admin

# Register your models here.
from .models import Employee, Device, History


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "employee_id", "email_id"]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "model"]


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ["id", "emp", "dev", "time"]


# def current_user_name(self, instance):
#     return instance.current_user.name
