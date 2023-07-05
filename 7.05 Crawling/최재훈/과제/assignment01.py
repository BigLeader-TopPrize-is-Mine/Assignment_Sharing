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


# import chromedriver_autoinstaller as ca
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import time, os, sys

# # driver = webdriver.Chrome(ca.install()) # chrome driver를 제어

# def ts(x) : # time sleep 함수
#     time.sleep(x)


# # 웹사이트 오픈하고 닫기
# ca.install()
# driver = webdriver.Chrome()
# driver.get('https://korean.visitkorea.or.kr')
# driver.maximize_window()

# # 검색창 클릭
# driver.find_element(By.XPATH, '//*[@id="placeHolder"]/a').click()
# ts(2)

# # 검색창에 검색어 넣고 조회
# driver.find_element(By.ID, 'inp_search').send_keys('여름여행'+'\n')
# ts(2)

# # 옵션 -> 강원 -> 확인 클릭
# driver.find_element(By.XPATH, '//*[@id="sorting_options"]/button[4]/span').click()
# driver.find_element(By.XPATH, '//*[@id="32"]/button/span').click()
# driver.find_element(By.XPATH, '//*[@id="contents"]/div/div[1]/div[3]/div[3]/div[2]/a[1]').click()
# ts(2)

# # 웹데이터 가져오기
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # 웹데이터 파싱하기
# title = soup.find('div', {'id':'listBody'}).find_all('div','tit')

# print(title)

# # 파일로 저장하기
# f_name = './title.txt'

# orig = sys.stdout

# with open(f_name, 'a', encoding='UTF-8') as file:
#     sys.stdout = file

#     for i in title:
#         print(i.get_text().strip())

# sys.stdout = orig

# print('데이터 수집이 정상적으로 완료되었습니다')

# ts(2); driver.close()