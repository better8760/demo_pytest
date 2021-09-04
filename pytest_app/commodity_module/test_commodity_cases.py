import pytest
import allure
@allure.epic("[epic]电商系统")
@allure.feature("[feature]商品模块")
@allure.story("[story]购买实物商品场景")
class TestCommodityCases:
    @allure.testcase("https://www.baidu.com",name="商品购买地址")
    @allure.issue("https://www.baidu.com",name="BUG地址")
    @allure.link("https://www.baidu.com",name="其他说明地址")
    @allure.title('购买首页商品')
    @allure.severity("blocker")
    def test_commodity_cases_01(self,set_up_module):
        with allure.step("1.进入首页"):
                1==True
        with allure.step("2.点击第一个商品"):
                1 == True
        print("exce TestCommodityCases  test_commodity_cases_01")
        assert True

    @pytest.mark.smoketest
    @pytest.mark.commoditytest
    def test_commodity_cases_02(self):
        print("exce TestCommodityCases  test_commodity_cases_02")
        assert True