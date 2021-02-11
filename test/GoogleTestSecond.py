import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleTestSecond(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")
        input = self.driver.find_element_by_name("q")
        input.send_keys("selenium" + Keys.ENTER)

    def test_search_term(self):
        assert 'Your search - Selenium - did not match any documents.' not in self.driver.page_source

    def test_text_present(self):
        results = self.driver.find_elements_by_class_name("g")
        assert "Selenium - Web Browser Automation" in results[0].text

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()