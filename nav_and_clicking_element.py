# https://techwithtim.net

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH = r"C:\Users\DUYEN\Desktop\chromedriver.exe"
page = r"https://techwithtim.net"

driver = webdriver.Chrome(PATH)
driver.get(page)

# all source code
# print(driver.page_source)

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    link_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    link_text.click()

    link_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    link_text.click()

    driver.back()
    driver.back()
    driver.forward()

except:
    driver.quit()
