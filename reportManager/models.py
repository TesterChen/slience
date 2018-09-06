from django.db import models

class Report(models.Model):
    name=models.CharField(max_length=40, null=False)
    start_at = models.CharField(max_length=40, null=True)
    status = models.BooleanField()
    testsRun = models.IntegerField()
    successes = models.IntegerField()
    
    class Meta:
        verbose_name = "测试报告"
        db_table = "Reports"


# Create your models here.
