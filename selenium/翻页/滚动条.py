#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
wd=webdriver.Chrome()
url="http://blog.csdn.net/otianye"
def open_URL(wd,url): 
    wd.get(url)
open_URL(wd,url)
#将页面滚动条拖到底部
def e_click(wd):
    js="var q=document.documentElement.scrollTop=1000"
    wd.execute_script(js)
    wd.find_element(By.LINK_TEXT,'web环境常见组合及管理后台').click()
'''
#若要对页面中的内嵌窗口中的滚动条进行操作，要先定位到该内嵌窗口，在进行滚动条操作
js="var q=document.getElementById('id').scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
'''
def B_quit(wd):
    wd.quit()
e_click(wd)
B_quit(wd)
