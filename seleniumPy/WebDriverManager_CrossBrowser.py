import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserName = input("enter browser name: ")

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("please enter a valid browser name")
    raise Exception("Driver Not Found")

driver.get("https://app.hubspot.com")

driver.implicitly_wait(5)

driver.find_element(By.ID,"username").send_keys("name123@gmail.com")
driver.find_element(By.ID,"password").send_keys("TestingIsCool123")
driver.find_element(By.ID,"loginBtn").click()

time.sleep(5)
driver.quit()