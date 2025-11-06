from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://www.wikipedia.org/")
print(driver.title)

searchbox = driver.find_element(By.ID, "searchInput")
searchbox.send_keys("Selenium (software)")
driver.implicitly_wait(3)
searchbox.click()
driver.implicitly_wait(3)

print(driver.title)
driver.quit()
