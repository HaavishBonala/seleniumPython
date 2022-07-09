from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
driver.get("https://www.haavish.com")
print(driver.title)

driver.find_element(By.XPATH, '''//*[@id="atIdViewHeader"]/div/div[2]/div[1]/div[2]/div/span/span''').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,
                    '''//*[@id="yDmH0d"]/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/input''').send_keys(
    "youtube")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,
                    '''//*[@id="yDmH0d"]/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/span[1]/div[1]/span/span/svg''').click()
