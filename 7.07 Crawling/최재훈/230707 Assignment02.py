from bs4 import BeautifulSoup
import chromedriver_autoinstaller as ca
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math
import time, os, re

def parse_Join(target):
    tmp = re.findall('>(.*?)<', target)
    res = ''.join(tmp)
    return res

query_txt = input('1. 검색어는? : ')
cnt = int(input('2. 건수는? : '))
page_cnt = math.ceil(cnt/7)
post_cnt = 1

# # 웹사이트 오픈하고 닫기
ca.install()
driver = webdriver.Chrome()
driver.get(f'https://section.blog.naver.com/Search/Post.naver?pageNo={page_cnt}&rangeType=ALL&orderBy=sim&keyword='+query_txt)
driver.maximize_window()

for step in range(1, page_cnt+1):

    now = "./"+time.strftime('%Y%m%d_%H%M%S')+'-'+query_txt
    os.makedirs(now)
    os.chdir(now)

    # # 웹데이터 가져오기
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # # 웹데이터 파싱하기
    title = soup.find('div', 'area_list_search').find_all('span', {'ng-bind-html': 'post.title'})
    # print(title)

    for idx, item in enumerate(title):
        if post_cnt > cnt:
            break
        item = parse_Join(str(item))
        print(f"{post_cnt}번 게시물 : {item}")
        post_cnt += 1

    step += 1
    try:
        driver.find_element(By.LINK_TEXT, "%s"% (step)).click()
    except:
        break

print('데이터 수집이 정상적으로 완료되었습니다')

time.sleep(3)
driver.close()