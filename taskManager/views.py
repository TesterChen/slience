from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from djcelery.models import CrontabSchedule,PeriodicTask
from taskManager.serialzers import PeriodicTaskSerializer,CrontabScheduleSerializer
# Create your views here.

class PeriodicViewSet(viewsets.ModelViewSet):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer
    permission_classes = (IsAuthenticated,)

class CrontabScheduleViewSet(viewsets.ModelViewSet):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer
    permission_classes = (IsAuthenticated,)