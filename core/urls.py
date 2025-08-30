from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import tasksViewSet , UserViewSet

router = DefaultRouter()
router.register(r'tasks', tasksViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
