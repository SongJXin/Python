#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url="https://www.baidu.com/"
keyword='福哥杂技 CSDN'
def open_Chrome(url):
    wd=webdriver.Firefox()
    wd.get(url)
    return wd

wd=open_Chrome(url)
def search_from_baidu(keyword):
    wd.find_element(By.ID,'kw').send_keys(keyword)
    wd.find_element(By.ID,'su').click()

search_from_baidu(keyword)
time.sleep(10)
wd.quit()



