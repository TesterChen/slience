from django.shortcuts import render
from rest_framework import viewsets,views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from djcelery.models import CrontabSchedule,PeriodicTask
from taskManager.serialzers import PeriodicTaskSerializer,CrontabScheduleSerializer

from taskManager.tasks import main_run
# Create your views here.

class PeriodicViewSet(viewsets.ModelViewSet):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer
    permission_classes = (IsAuthenticated,)

class CrontabScheduleViewSet(viewsets.ModelViewSet):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer
    permission_classes = (IsAuthenticated,)
    # http_method_names = ["get","post","delete"]
    

class RunTestView(views.APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self,request):
        main_run.apply_async(queue='default')
        return Response(status=204)
