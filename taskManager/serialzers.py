from djcelery.models import PeriodicTask,CrontabSchedule
from rest_framework import serializers

class PeriodicTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = ('name','task','crontab','enabled','kwargs','queue','description')

class CrontabScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrontabSchedule
        fields = ('minute','hour','day_of_week','day_of_month','month_of_year')
