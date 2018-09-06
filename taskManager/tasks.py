# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from taskManager.utils.scripts_version_control import update_code
from taskManager.utils.allure_report import generate_report,output_filename,upload_report
from robot import run
import os

#一期先硬编码,待项目管理功能开发完成后由task入参
repo_name = 'PxnAutoTest'
repo_url = 'git://github.com/PengfeiInPxn/PxnAutoTest.git'



@shared_task(bind=True)
def main_run(self):
    #更新脚本
    script_path=update_code(repo_name,repo_url)
    #执行脚本
    # run(repo_path+'Scripts/',listener=allure_robotframework())
    run(script_path,xunit=output_filename,report=None,log=None,output=None)
    #构建报告
    generate_report()
    #上传报告
    upload_report("http://127.0.0.1:8000/upload/%s" % self.request.id)
    #发送报告


if __name__ =="__main__":
    from celery import Celery
    main_run(Celery())