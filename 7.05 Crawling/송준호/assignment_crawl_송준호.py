import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.action_chains import *

driver = webdriver.Chrome() 
driver.get("https://korean.visitkorea.or.kr")

driver.set_window_size(1024, 768)

driver.find_element(By.ID,'inp_search_mo').click()
driver.find_element(By.ID,'inp_search').send_keys("여름여행")

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

driver.maximize_window()

driver.find_element(By.CLASS_NAME,'option').click()
driver.find_element(By.XPATH, '//*[@id="32"]/button').click()
driver.find_element(By.XPATH,'//*[@id="contents"]/div/div[1]/div[3]/div[3]/div[2]/a[1]').click()

soup = BeautifulSoup(driver.page_source,'html.parser')
src = []

found = soup.find('div',{"id":"listBody"}).find_all("div","tit")
print(found)

time.sleep(5)
driver.quit()