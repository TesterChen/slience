from reportManager.models import Report
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('id','name','start_at','status','testsRun','successes','task_id')