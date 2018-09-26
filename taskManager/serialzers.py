from djcelery.models import PeriodicTask,CrontabSchedule
from rest_framework import serializers

class CrontabScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrontabSchedule
        fields = ('minute','hour','day_of_week','day_of_month','month_of_year')


#http://www.django-rest-framework.org/api-guide/serializers/#serializer-extensions
class PeriodicTaskSerializer(serializers.HyperlinkedModelSerializer):
    crontab = CrontabScheduleSerializer(many=False)

    class Meta:
        model = PeriodicTask
        fields = ('name','task','crontab','enabled','kwargs','queue','description')

    def create(self,validated_data):
        crontab_data = validated_data.pop('crontab')
        crontab = CrontabSchedule.objects.create(**crontab_data)
        task = PeriodicTask.objects.create(crontab=crontab,**validated_data)
        return task