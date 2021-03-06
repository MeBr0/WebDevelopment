from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Task
from api.serializers import TaskSerializer


class TasksView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, )

    # filters by pk of task_list
    def get_queryset(self):
        return Task.objects.filter(task_list=self.kwargs['pk'])

    def get_serializer_class(self):
        return TaskSerializer


class TaskView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, )

    # filter by pk2 of task_list, by pk of task
    def get_queryset(self):
        print(self.args)

        return Task.objects.filter(id=self.kwargs['pk'], task_list=self.kwargs['pk2'])

    def get_serializer_class(self):
        return TaskSerializer

