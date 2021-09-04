import pytest


class TestLoginCases:
    @pytest.mark.smoketest
    def test_login_cases_01(self):
        print("exce TestLoginCases  test_login_cases_01")
        assert True
    @pytest.mark.skipif(condition=(r for r in range(10) if r>0),reason="测试跳过")
    def test_login_cases_02(self):
        print("exce TestLoginCases  test_login_cases_02")
        assert True

