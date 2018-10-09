from subprocess import  Popen
import os
import platform
import zipfile
import requests
import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from slience.settings import EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD

EMAIL_SEND_USERNAME = 'pxnonetest@gmail.com'  # 定时任务报告发送邮箱，支持163,qq,sina,企业qq邮箱等，注意需要开通smtp服务
EMAIL_SEND_PASSWORD = 'test@pxn.one'     # 邮箱密码

cur_path= os.path.split(os.path.realpath(__file__))[0]
output_path=os.path.join(cur_path,"outputs")
xunit_output_filename=os.path.join(output_path,"xunit_output.xml")
output_filename=os.path.join(output_path,"output.xml")
allure_path=os.path.join(cur_path,"allure","bin","allure.bat") if platform.system() == "Windows" else os.path.join(cur_path,"allure","bin","allure")
report_path=os.path.join(cur_path,"reports")
report_filename=os.path.join(cur_path,"report.zip")
def generate_report():
    process = Popen((allure_path,"generate",output_path,"-c","-o",report_path))
    process.wait()
    zf = zipfile.ZipFile(report_filename,"w")
    try:
        for root,dirs,files in os.walk(report_path):
            for d in dirs:
                d_path=os.path.join(root,d)
                arc_path=os.path.relpath(d_path,report_path)
                zf.write(d_path,arc_path)
            for f in files:
                f_path=os.path.join(root,f)
                arc_path=os.path.relpath(f_path,report_path)
                zf.write(f_path,arc_path)
    finally:
        zf.close()

def upload_report(url,task_id):
    # data = {
    #         "name" :task_name,
    #         "start_at" : result.suite.starttime,
    #         "status" : result.suite.passed,
    #         "total" : result.suite.statistics.all.total,
    #         "successes" : result.suite.statistics.all.passed,
    #         "task_id" : task_id,
    #         "file":open(report_filename,"rb"),
    #     }
    files= {
        "file":open(report_filename,"rb"),
        }
    # headers = {
    #     "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundarydEWZnenjYLlunuJP"
    # }
    r = requests.put(url+task_id,files=files,auth=('yaopengfei@pxn.one', 'wodeshijie123'))

def upload_result(task_name,url,task_id,result):

    #20181009 09:11:02.037
    #2018-09-27T00:12:00Z
    start_at_time_struct=time.strptime(result.suite.starttime,"%Y%m%d %H:%M:%S.%f")
    start_at=time.strftime("%Y-%m-%dT%H:%M:%SZ",start_at_time_struct)
    
    data = {
            "name" :task_name,
            "start_at" : start_at,
            "status" : result.suite.passed,
            "total" : result.suite.statistics.all.total,
            "successes" : result.suite.statistics.all.passed,
            "task_id" : task_id,
        }
    r = requests.post(url,json=data,auth=('yaopengfei@pxn.one', 'wodeshijie123'))


def send_email_report(taskinfo,results,url):
    
    smtp_server='smtp.gmail.com'
    body = MIMEText("附件为定时任务生成的接口测试报告，请查收，谢谢！", _subtype='html', _charset='utf-8')
    
    msg = MIMEMultipart()
    msg['Subject'] = taskinfo['subject']
    msg['from'] = EMAIL_SEND_USERNAME
    msg['to'] = taskinfo['recevers']
    msg.attach(body)

    smtp = smtplib.SMTP(smtp_server,587)
    smtp.starttls()
    smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)
    smtp.sendmail(EMAIL_SEND_USERNAME, taskinfo['recevers'].split(','), msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    taskinfo={
        "subject":"hello",
        "recevers":"yaopengfei@pxn.one,yaopengfei+test@pxn.one"
    }
    send_email_report(taskinfo,None,None)