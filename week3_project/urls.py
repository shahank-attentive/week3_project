from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("employeeapi", views.EmployeeModelViewSet)
router.register("deviceapi", views.DeviceModelViewSet)
# router.register("changes", views.get_changes)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
