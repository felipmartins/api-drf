from rest_framework import routers
from todo.views import TaskViewSet, UserViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("api/", include(router.urls))
]
