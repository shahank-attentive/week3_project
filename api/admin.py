from django.contrib import admin

# Register your models here.
from .models import Employee, Device


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "employee_id", "email_id"]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "model", "current_user"]

    # def current_user_name(self, instance):
    #     return instance.current_user.name
