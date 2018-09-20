from django.db import models

class Report(models.Model):
    name=models.CharField(max_length=40,null=True)
    start_at = models.DateTimeField(null=True)
    status = models.BooleanField()
    testsRun = models.IntegerField()
    successes = models.IntegerField()
    task_id = models.CharField(max_length=32,null=True)
    class Meta:
        verbose_name = "测试报告"
        db_table = "Reports"


# Create your models here.
