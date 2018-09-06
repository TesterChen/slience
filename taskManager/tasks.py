# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from taskManager.utils.scripts_version_control import update_code
from taskManager.utils.allure_report import generate_report,output_filename,upload_report
from robot import run
import os
import uuid

#一期先硬编码,待项目管理功能开发完成后由task入参
repo_name = 'PxnAutoTest'
repo_url = 'git://github.com/PengfeiInPxn/PxnAutoTest.git'



@shared_task
def main_run():
    report_id=uuid.uuid1()
    #更新脚本
    script_path=update_code(repo_name,repo_url)
    #执行脚本
    # run(repo_path+'Scripts/',listener=allure_robotframework())
    run(script_path,xunit=output_filename,report=None,log=None,output=None)
    #构建报告
    generate_report()
    #上传报告
    upload_report("http://127.0.0.1:8000/upload/%s" % report_id)
    #发送报告

    return report_id

if __name__ =="__main__":
    main_run()