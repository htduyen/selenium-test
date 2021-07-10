import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        PATH = r"C:\Users\DUYEN\Desktop\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://phptravels.com/demo/")
        self.assertIn("Demo", driver.title)
        element = driver.find_element_by_class_name("dropdown-content")
        options = element.find_elements_by_class_name("lvl-1")
        for option in options:
            print(option.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
