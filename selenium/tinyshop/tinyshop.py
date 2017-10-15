#coding=utf-8
from click_and_input import *
from selenium import webdriver

wd=webdriver.Chrome()
url="http://172.18.24.42/tinyshop/"
open_URL(wd,url)
e_click_by_link(wd,'登录')
input_by_id(wd,'account','s123@123.123')
input_by_xpath(wd,'/html/body/div[2]/div/div/form/ul/li[2]/input','123456')
e_click_by_xpath(wd,'/html/body/div[2]/div/div/form/ul/li[4]/button')
if is_element_exist(wd,"安全退出"):
    print("login successful")
    wd.get_screenshot_as_file("successful.png")
else:
    print("login failed")
    wd.get_screenshot_as_file("failed.png")
Brower_quit(wd)
