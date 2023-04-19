from rest_framework import viewsets
from todo.models import User, Task
from todo.serializer import UserSerializer, TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False)
    def in_progress(self, request):
        in_progress_tasks = Task.objects.filter(status=False)
        serializer = self.get_serializer(in_progress_tasks, many=True)
        return Response(serializer.data)
