# https://techwithtim.net
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH = r"C:\Users\DUYEN\Desktop\chromedriver.exe"
page = r"https://techwithtim.net"

driver = webdriver.Chrome(PATH)
driver.get(page)
print(driver.title)
assert "Tech With Tim" in driver.title
elem = driver.find_element_by_name("s")
elem.clear()
elem.send_keys("test")
elem.send_keys(Keys.RETURN)

# all source code
# print(driver.page_source)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text)
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-header   ")
        print(header.text)
except:
    driver.quit()
finally:
    driver.quit()

