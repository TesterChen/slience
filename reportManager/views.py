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

class ReportFileView(views.APIView):
    permission_classes = (AllowAny,)
    parser_classes = (FileUploadParser,)

    def put(self,request,filename,format=None):
        file_obj = request.data['file']
        zf = zipfile.ZipFile(file_obj)
        zf.extractall(path='reports/%s' % filename)
        return Response(status=204)
# Create your views here.
