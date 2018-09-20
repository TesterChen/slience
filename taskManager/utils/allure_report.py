from subprocess import  Popen
import os
import platform
import zipfile
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from slience.settings import EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD

EMAIL_SEND_USERNAME = 'pxnonetest@gmail.com'  # 定时任务报告发送邮箱，支持163,qq,sina,企业qq邮箱等，注意需要开通smtp服务
EMAIL_SEND_PASSWORD = 'test@pxn.one'     # 邮箱密码

cur_path= os.path.split(os.path.realpath(__file__))[0]
output_path=os.path.join(cur_path,"outputs")
output_filename=os.path.join(output_path,"xunit_output.xml")
allure_path=os.path.join(cur_path,"allure","bin","allure.bat") if platform.system() == "Windows" else os.path.join(cur_path,"allure","bin","allure")
report_path=os.path.join(cur_path,"reports")
report_filename=os.path.join(cur_path,"report.zip")
def generate_report():
    process = Popen("%s generate %s -c -o %s" % (allure_path,output_path,report_path))
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

def upload_report(url):
    r = requests.put(url,files={"file":open(report_filename,"rb"),})

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