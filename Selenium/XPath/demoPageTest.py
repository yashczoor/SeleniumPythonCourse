from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"C:\Users\Piotr Jaroszuk\PycharmProjects\SeleniumPythonOdPodstaw\SeleniumPythonCourse\Selenium\XPath\Test.html")

driver.find_element_by_xpath("/html/body/table/tbody/tr/th")
driver.find_element_by_xpath("//tbody//th")
driver.find_element_by_xpath("//th")
driver.find_element_by_xpath("//th[text()='Month']")
driver.find_element_by_xpath("//button[@id='clickOnMe']")
print(driver.find_element_by_xpath("//input[@name='fname']/following-sibling::table").text)
print()
intListElementsLength = len(driver.find_elements_by_xpath("//th")) #zwróci listę obiektów
print(intListElementsLength)

driver.quit()