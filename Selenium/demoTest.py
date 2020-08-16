from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"C:\Users\Piotr Jaroszuk\PycharmProjects\SeleniumTutorial\Test.html")
# driver.maximize_window()
# driver.find_element_by_id("newPage").click()
# driver.quit()
# driver.close() #zamyka okno na którym jest focus
driver.find_element_by_id('fname').click()
# driver.find_element_by_id('tego nie ma') #nie ma to błąd NoSuchElementException
driver.find_element(By.ID,"fname")
driver.find_element(By.ID,"clickOnMe")
driver.find_element_by_name('fname')
driver.find_element_by_link_text('Visit W3Schools.com!')
driver.find_element_by_partial_link_text('W3')
driver.find_element_by_class_name('topSecret') #obiekt może mieć więcej klas. Moge lokalizować po jednej z nich
driver.quit()