from bs4 import BeautifulSoup
import chromedriver_autoinstaller as ca
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time, os

query_txt = input('1. 크롤링할 이미지의 키워드? : ')
cnt = int(input('2. 크롤링할 건수는? : '))

now = "./"+time.strftime('%Y%m%d_%H%M%S')+'-'+query_txt
os.makedirs(now)
os.chdir(now)

try:
    ca.install()
    driver = webdriver.Chrome()
except FileNotFoundError as err:
    print(f'크롬 브라우저를 찾을 수 없습니다.')

base_link = 'https://search.naver.com/search.naver?where=image&sm=tab_hum&query='
driver.get(base_link+query_txt)
driver.maximize_window()

# for i in range(6):
#     time.sleep(3)
#     driver.find_element()
#     driver.find_element_by_xpath('//body').send_keys(Keys.END)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_src=[]

for i in soup.find_all('img', class_='_image _listImage'):
    img_src.append(i['src'])

for idx, save_img in enumerate(img_src, start=1):
    urllib.request.urlretrieve(save_img, str(idx)+".jpg")
    print(f'{idx}은 {save_img}입니다.')
    if idx==cnt:
        break

time.sleep(2)
driver.quit()