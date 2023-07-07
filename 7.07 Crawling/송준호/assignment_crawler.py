import time, os, re

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.action_chains import *


import math



# driver = webdriver.Chrome() 
# driver.get("https://korean.visitkorea.or.kr")

# driver.set_window_size(1024, 768)

# driver.find_element(By.ID,'inp_search_mo').click()
# driver.find_element(By.ID,'inp_search').send_keys("여름여행")

# actions = ActionChains(driver)
# actions.send_keys(Keys.ENTER)
# actions.perform()

# driver.maximize_window()

# driver.find_element(By.CLASS_NAME,'option').click()
# driver.find_element(By.XPATH, '//*[@id="32"]/button').click()
# driver.find_element(By.XPATH,'//*[@id="contents"]/div/div[1]/div[3]/div[3]/div[2]/a[1]').click()

# soup = BeautifulSoup(driver.page_source,'html.parser')
# src = []

# found = soup.find('div',{"id":"listBody"}).find_all("div","tit")
# with open('file.txt','w') as file_data:    
#     for txt in found :
#         file_data.writelines(txt.get_text())
#         file_data.write("\n")

# # soup.find_all('p)[1].get_text().strip()
# # soup.find_all('p)[1].get_text().strip().replace('text','txt')
# # enumerate(x,start=1)


# time.sleep(5)
# driver.quit()

# ==============================================================================================================

#arr
def parse_Join(target):
    tmp = re.findall('>(.*?)<', target)
    res = ''.join(tmp)
    return res

query_txt = input('1. 검색어는? : ')
cnt = int(input('2. 건수는? : '))
page_cnt = math.ceil(cnt/7)
post_cnt = 1

# # 웹사이트 오픈하고 닫기
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
