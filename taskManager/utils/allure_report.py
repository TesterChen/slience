from subprocess import  Popen
import os
import platform
import zipfile
import requests

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