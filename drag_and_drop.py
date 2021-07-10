import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        PATH = r"C:\Users\DUYEN\Desktop\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.testandquiz.com/selenium/testing.html")
        self.assertIn("Sample Test Page", driver.title)
        element = driver.find_element_by_link_text("This is a link")
        element.click()
        driver.back()

        element = driver.find_element_by_id("fname")
        element.send_keys("Huynh Thanh Duyen")

        btn_submit = driver.find_element_by_id("idOfButton").click()

        gender = driver.find_element_by_id("male").click()

        check_box = driver.find_element_by_class_name("Automation").click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
