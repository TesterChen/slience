from reportManager.models import Report
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('pk','url','name','start_at','status','total','successes','task_id')