import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleTestThird(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")
        input = self.driver.find_element_by_name("q")
        input.send_keys("selenium")
        time.sleep(1);


    def test_suggestion_exist(self):
        suggestions = self.driver.find_elements_by_xpath("//ul[@class='erkvQe' and @role='listbox']/li[@class='sbct' and @role='presentation']")
        assert len(suggestions) is 10

    def test_suggestions_start(self):
        suggestions = self.driver.find_elements_by_xpath("//ul[@class='erkvQe' and @role='listbox']")
        for suggestion in suggestions:
            assert "selenium" in suggestion.text

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()