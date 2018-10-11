# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from allure_robotframework.robot_listener import allure_robotframework

from taskManager.utils.scripts_version_control import update_code
from taskManager.utils.allure_report import generate_report,output_path,output_filename,upload_report,upload_result,send_email_report
from robot import run
from robot.api import ExecutionResult
import os

#一期先硬编码,待项目管理功能开发完成后由task入参
REPO_NAME = 'PxnAutoTest'
REPO_URL = 'git@github.com:pxn-qa-team/PxnAutoTest.git'
SERVER_URL = 'http://35.188.112.90'


@shared_task(bind=True)
def main_run(self,task_name="",reciever="",suite={"name":REPO_NAME,"url":REPO_URL}):
    #更新脚本
    script_path=update_code(suite)
    #执行脚本
    run(script_path,listener=allure_robotframework(output_path),output=output_filename)
    # result=run(script_path,xunit=output_filename,report=None,log=None,output=None)
    result = ExecutionResult(output_filename)
    #构建报告
    generate_report()
    #上传报告
    upload_report("%s/api/report-upload/" % SERVER_URL,self.request.id)
    #上传结果
    upload_result(task_name,"%s/api/reports/" % SERVER_URL,self.request.id,result)
    #发送报告
    if reciever:
        send_email_report({
            "subject":task_name+" 自动化测试报告",
            "recevers":reciever,
        },result,"%s/reports/%s" % (SERVER_URL,self.request.id))
