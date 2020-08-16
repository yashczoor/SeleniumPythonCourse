from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Test.html') #to get relative path of html file
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(filename)

driver.maximize_window()
driver.find_element_by_id("clickOnMe").click()

alert = driver.switch_to.alert
print("Alert says: " + alert.text)
time.sleep(2)
alert.accept()

driver.find_element_by_id("clickOnMe").click()
# clickMeButton = driver.find_element_by_id("clickOnMe")
# clickMeButton.click()
# driver.find_element_by_tag_name("p").click() #error, element is not visible
driver.switch_to.alert.dismiss() #like pressing Cancel

inputField = driver.find_element_by_id("fname")
inputField.send_keys("Piotr")
#send_keys allows to input strings




# driver.quit()