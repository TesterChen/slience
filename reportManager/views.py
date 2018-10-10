from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets,views
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.parsers import FileUploadParser

from reportManager.models import Report
from reportManager.serializers import ReportSerializer

import zipfile


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated,)
    filter_fields = ('name','status')


class ReportFileView(views.APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)
    # parser_classes = (MultiPartParser,)

    def put(self,request,filename,format=None):
        # print(request.data["file"])
        # kwdata = {
        #     "name" :request.data["name"],
        #     "start_at" : request.data["start_at"],
        #     "status" : request.data["status"],
        #     "total" : request.data["total"],
        #     "successes" : request.data["successes"],
        #     "task_id" : request.data["task_id"],
        # }

        file_obj = request.data['file']
        # task_id = request.data["task_id"]

        # report = Report.objects.get_or_create(**kwdata)
        # request.data[""]
        zf = zipfile.ZipFile(file_obj)
        zf.extractall(path='view_report/%s' % filename)
        return Response(status=204)
# Create your views here.
