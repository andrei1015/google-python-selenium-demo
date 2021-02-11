import unittest
import time
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys

class GoogleTestFifth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")
        input = self.driver.find_element_by_name("q")
        input.send_keys("selenium" + Keys.ENTER)

    def test_searchbar(self):
        search = self.driver.find_element_by_xpath('//div[@id="searchform"]')
        #print(search.value_of_css_property("position"))
        assert 'absolute' in search.value_of_css_property("position")

    def test_scroll(self):
        search = self.driver.find_element_by_xpath('//div[@id="searchform"]')
        nav = self.driver.find_element_by_xpath("//table[@id='nav']")
        nav.location_once_scrolled_into_view
        assert 'fixed' in search.value_of_css_property("position")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()