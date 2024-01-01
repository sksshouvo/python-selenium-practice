import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("file:///C:/Users/User/OneDrive/Desktop/python-selenium-practice/test-html/navigating.html")

element = driver.find_element(By.ID, "passwd-id")
# element = driver.find_element(By.NAME, "passwd")
# element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
# element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

# print(element.get_attribute('value'))
# element.clear()
# element.send_keys("some text")

# selectElement = driver.find_element(By.XPATH, "//select[@name='human_being']")
# all_options = selectElement.find_elements(By.TAG_NAME, "option")
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()

select = Select(driver.find_element(By.NAME, 'human_being'))
select.select_by_value("female")

time.sleep(10)
driver.close()