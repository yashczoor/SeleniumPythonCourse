from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
driver.set_window_size(1800,1200)
# driver.maximize_window() #może do testów nie najlepiej bo może różnie wychodzić na różnych kompach
# driver.minimize_window()
driver.close()



