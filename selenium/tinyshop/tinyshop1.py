#coding=utf-8
import click_and_input
from selenium import webdriver

wd=webdriver.Chrome()
url="http://172.18.24.42/tinyshop/"
open_URL(wd,url)
e_click_by_link(wd,'登录')
input_by_id(wd,'account','s123@123.123')
input_by_xpath(wd,'/html/body/div[2]/div/div/form/ul/li[2]/input','123456')
e_click_by_xpath(wd,'/html/body/div[2]/div/div/form/ul/li[4]/button')
Brower_quit(wd)
