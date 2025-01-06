from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, TaskViewSet, InvoiceViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]