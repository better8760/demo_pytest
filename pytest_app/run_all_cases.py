import pytest
import os
import allure
import shutil

report_path=os.path.dirname(__file__)+'./allure_xml_report'
report_html_path=os.path.dirname(__file__)+'./allure_html_report'
if os.path.isdir(report_path):
    shutil.rmtree(report_path)
    os.mkdir(report_path)
#pytest.main(["-s","-v","--alluredir=%s"%report_path,"--allure-stories=[story]购买实物商品场景"])
pytest.main(["-s","-v","--alluredir=%s"%report_path,"--allure-severities=blocker"])
os.system('allure generate %s -o %s --clean'%(report_path,report_html_path))
