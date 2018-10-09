# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from allure_robotframework.robot_listener import allure_robotframework

from taskManager.utils.scripts_version_control import update_code
from taskManager.utils.allure_report import generate_report,output_path,output_filename,upload_report,upload_result
from robot import run
from robot.api import ExecutionResult
import os

#一期先硬编码,待项目管理功能开发完成后由task入参
repo_name = 'PxnAutoTest'
repo_url = 'git://github.com/PengfeiInPxn/PxnAutoTest.git'



@shared_task(bind=True)
def main_run(self,task_name="",reciever="",suite={"name":repo_name,"url":repo_url}):
    #更新脚本
    script_path=update_code(suite)
    #执行脚本
    run(script_path,listener=allure_robotframework(output_path),output=output_filename)
    # result=run(script_path,xunit=output_filename,report=None,log=None,output=None)
    result = ExecutionResult(output_filename)
    #构建报告
    generate_report()
    #上传报告
    upload_report("http://127.0.0.1:1234/api/report-upload/",self.request.id)
    #上传结果
    upload_result(task_name,"http://127.0.0.1:1234/api/reports/",self.request.id,result)
    #发送报告

