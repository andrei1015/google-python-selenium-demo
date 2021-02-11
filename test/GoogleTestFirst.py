import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleTestFirst(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")

    def test_search_input(self):
        self.driver.find_element_by_name("q")

    def test_search_button(self):
        self.driver.find_element_by_name("btnK")

    def test_feeling_lucky(self):
        self.driver.find_element_by_name("btnI")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()