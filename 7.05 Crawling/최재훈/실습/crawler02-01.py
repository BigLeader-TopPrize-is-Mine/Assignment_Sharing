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

pre_link = 'https://www.google.com/search?q='
low_link = '&hl=EN&tbm=isch&sclient=img'
driver.get(pre_link+query_txt+low_link)
driver.maximize_window()

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_src=[]

tmp = 0
for i in soup.find_all('img', class_='rg_i Q4LuWd'):
    if tmp != cnt:
        print(f"DATA : {i['src']}")
        print("\n")
        img_src.append(i['src'])
        tmp += 1

for idx, save_img in enumerate(img_src, start=1):
    urllib.request.urlretrieve(save_img, str(idx)+".jpg")
    print(f'{idx}은 {save_img}입니다.')
    if idx==cnt:
        break

time.sleep(2)
driver.quit()