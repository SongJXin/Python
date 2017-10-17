#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#web页面翻页 - 1 ：  PAGE-DOWN
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

wd=webdriver.Chrome()
url="http://172.18.24.42/tinyshop/"
def open_URL(wd,url): 
    wd.get(url)
open_URL(wd,url)

def e_click(wd):
    wd.find_element(By.LINK_TEXT,'售后保障').click()

'''
#若要对页面中的内嵌窗口中的滚动条进行操作，要先定位到该内嵌窗口，在进行滚动条操作
js="var q=document.getElementById('id').scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
'''
def B_quit(wd):
    time.sleep(10)
    wd.quit()
while 1==1:
    try:
        e_click(wd)
        break
    except Exception as err:
        ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
B_quit(wd)
