#coding=utf-8
from click_and_input import *
from selenium import webdriver

wd=webdriver.Firefox()
url="http://172.18.24.42/tinyshop/"
open_URL(wd,url)
e_click_by_link(wd,'登录')

username_passwd=[['123@123.123','123456',False],['132','123',False],['s123@123.123','123456',True]]
for item in username_passwd:
    input_by_id(wd,'account',item[0])
    input_by_xpath(wd,'/html/body/div[2]/div/div/form/ul/li[2]/input',item[1])
    e_click_by_xpath(wd,'/html/body/div[2]/div/div/form/ul/li[4]/button')
    if is_element_exist(wd,'安全退出') == item[2]:
        print ("pass")
    else:
        print ("failed")
    if is_element_exist(wd,"安全退出"):
        break
e_click_by_link(wd,'安全退出')
Brower_quit(wd)
