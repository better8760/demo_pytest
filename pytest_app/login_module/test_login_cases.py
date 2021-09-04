import pytest
import allure
import os
class TestLoginCases:
    @pytest.mark.smoketest
    def test_login_cases_01(self):
        with open(os.path.dirname(__file__)+'/screen_shot/ss.png','rb') as file:
            img_file=file.read()
            allure.attach(img_file, '图片附件', allure.attachment_type.PNG)
        print("exce TestLoginCases  test_login_cases_01")
        assert True
    @pytest.mark.skipif(condition=(r for r in range(10) if r>0),reason="测试跳过")
    def test_login_cases_02(self):
        print("exce TestLoginCases  test_login_cases_02")
        assert True