from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework import filters


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)

    filter_field = ('completed',)
    ordering = ('-date_created',)
    search_field = ('=task_name',)
