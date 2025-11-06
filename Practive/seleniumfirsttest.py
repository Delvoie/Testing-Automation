from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ai.google.dev/")
print(driver.title)

driver.quit()
