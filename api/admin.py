from django.contrib import admin

# Register your models here.
from .models import Employee, Device, History, Status


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "employee_id", "email_id"]

    # def __str__(self) -> str:
    #     return self.name


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "model", "current_user"]

    def current_user(self, obj):
        return "\n".join([emp.name for emp in obj.current_user.all()])


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["id", "emp", "dev", "time"]


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ["id", "emp", "dev", "time"]


# def current_user_name(self, instance):
#     return instance.current_user.name
