from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.imdb.com/")


search_input = driver.find_element(By.ID, "suggestion-search")
search_input.send_keys("pulp fiction")
search_input.send_keys(Keys.RETURN)

time.sleep(6)

driver.quit()
