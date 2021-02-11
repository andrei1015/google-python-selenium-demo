import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleTestFourth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")
        input = self.driver.find_element_by_name("q")
        input.send_keys("selenium" + Keys.ENTER)
        next = self.driver.find_element_by_xpath("//table[@id='nav']//td[@class='b navend' and @role='heading']")
        next.click()

    def test_nav(self):
        navs = self.driver.find_elements_by_xpath("//table[@id='nav']//td[not(@class) or @class='cur']")
        assert 'cur' in navs[1].get_attribute("outerHTML")

    def test_back(self):
        previous = self.driver.find_element_by_xpath("//table[@id='nav']//td[@class='b navend' and @role='heading']")
        previous.click()
        navs = self.driver.find_elements_by_xpath("//table[@id='nav']//td[not(@class) or @class='cur']")
        assert 'cur' in navs[0].get_attribute("outerHTML")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()