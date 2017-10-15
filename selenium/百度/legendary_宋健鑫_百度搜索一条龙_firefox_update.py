#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
wd=webdriver.Firefox()
url="https://www.baidu.com/"
def open_URL(wd,url): 
    wd.get(url)


def search_from_baidu(keyword):
    kw.send_keys(keyword)
    su.click()

open_URL(wd,url)
kw=wd.find_element(By.ID,'kw')
su=wd.find_element(By.ID,'su')
search_from_baidu('福哥杂技 CSDN')

time.sleep(10)
kw.clear()
search_from_baidu('2017放假安排')
time.sleep(10)
url='http://blog.csdn.net/otianye/article/details/78092614'
open_URL(wd,url)

time.sleep(10)
wd.back()
time.sleep(10)
wd.quit()




