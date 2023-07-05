from selenium import webdriver
import chromedriver_autoinstaller as ca
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, os, sys

try:
    ca.install()
    driver = webdriver.Chrome()
except FileNotFoundError as err:
    print(f'크롬 브라우저를 찾을 수 없습니다.')


driver.get('https://www.riss.kr')
driver.maximize_window()

# 접속 후 팝업창이 있으면 모두 제거하기 #
main = driver.window_handles # 열린 창 개수 main에 저장한다.
for handle in main: # 열린 창 개수만큼 순회하면서 메인창을 제외하곤 다 닫는다.
    if handle != main[0]:
        driver.switch_to.window(handle)
        driver.close()

# 원래 창으로 돌아가기
driver.switch_to.window(driver.window_handles[0]) # ...handles[0]이 메인창이다.

time.sleep(2)
driver.find_element(By.ID, 'query').send_keys('빅데이터'+'\n')

# 학위논문 클릭하기
time.sleep(2)
driver.find_element(By.LINK_TEXT, '학위논문').click()

soup = BeautifulSoup(driver.page_source, 'html.parser')
title = soup.find('div', 'srchResultListW').find_all('p', 'title')
for i in title:
    print(i.get_text().strip())

f_name = './riss.txt'
original = sys.stdout

with open(f_name, 'a', encoding='UTF-8') as file:
    sys.stdout = file

    for i in title:
        print(i.get_text().strip())

sys.stdout = original

print(f'데이터 수집이 정상적으로 완료되었습니다.')
print(f'수집된 결과는 {f_name}에 저장되었습니다.')

# 웹사이트 닫기
time.sleep(2)
driver.close()
