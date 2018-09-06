from reportManager.models import Report
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ReportSerializer(serializers.Serializer):
    class Meta:
        model = Report
        fields = ('name','start_at','status','testsRun','successes')