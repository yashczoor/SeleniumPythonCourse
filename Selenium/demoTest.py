from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"C:\Users\Piotr Jaroszuk\PycharmProjects\SeleniumTutorial\Test.html")
# driver.maximize_window()
# driver.minimize_window()
# driver.quit()
# driver.close() #zamyka okno na którym jest focus

# driver.find_element_by_id("newPage").click()
driver.find_element_by_id('fname').click()
# driver.find_element_by_id('tego nie ma') #nie ma to błąd NoSuchElementException
driver.find_element(By.ID,"fname")
driver.find_element(By.ID,"clickOnMe")

driver.find_element_by_name('fname')

driver.find_element_by_link_text('Visit W3Schools.com!')
driver.find_element_by_partial_link_text('W3')

driver.find_element_by_class_name('topSecret') #obiekt może mieć więcej klas. Moge lokalizować po jednej z nich

driver.find_element_by_tag_name("a")
driver.find_element_by_tag_name("p")
# driver.find_element_by_tag_name("div") #brak tagu div na stronie testowej

driver.find_element_by_css_selector("a")
driver.find_element_by_css_selector("img#smileImage")
driver.find_element_by_css_selector("p.topSecret")

print(driver.find_element_by_css_selector("td:first-child").text)
print(driver.find_element_by_css_selector("th:first-child").text)
print(driver.find_element_by_css_selector("input[type=password]:nth-child(5)").get_property("value"))





driver.quit()