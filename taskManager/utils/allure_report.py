from subprocess import  Popen
import os
import platform

cur_path= os.path.split(os.path.realpath(__file__))[0]
output_path=os.path.join(cur_path,"outputs")
output_filename=os.path.join(output_path,"xunit_output.xml")
allure_path=os.path.join(cur_path,"allure","bin","allure.bat") if platform.system() == "Windows" else os.path.join(cur_path,"allure","bin","allure")
report_path=os.path.join(cur_path,"reports")

def generate_report():
    process = Popen("%s generate %s -c -o %s" % (allure_path,output_path,report_path))
    process.wait()