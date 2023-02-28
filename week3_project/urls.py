from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("employeeapi", views.EmployeeModelViewSet)
router.register("deviceapi", views.DeviceModelViewSet)
router.register("employeehistory", views.EmployeeHistoryModelViewSet)
router.register("devicehistory", views.DeviceHistoryModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("devhistory/<int:pk>", views.DeviceHistoryModelViewSet.devicehistory),
]
