from selenium import webdriver
import chromedriver_autoinstaller as ca
from selenium.webdriver.common.by import By
import time

try:
    ca.install()
    driver = webdriver.Chrome()
except FileNotFoundError as err:
    print(f'크롬 브라우저를 찾을 수 없습니다.')

keyword = '여름여행'
driver.get(f'https://korean.visitkorea.or.kr/search/search_list.do?keyword={keyword}')
driver.maximize_window()

time.sleep(2)
driver.find_element(By.CLASS_NAME, 'option').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="32"]').click()

# 웹사이트 닫기
time.sleep(5)
driver.close()
