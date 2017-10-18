#coding=utf-8
from click_and_input import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

wd=webdriver.Firefox()
wd.maximize_window()
open_URL(wd,"http://www.baidu.com")

input_by_id(wd,"kw","福哥杂记 CSDN")
e_click_by_id(wd,"su")
e_click_by_partial_link(wd,u",软件生命周期中的攻防博弈 - ")
wd=switch_tab_page(wd)
e_click_by_partial_link(wd,u'登录')
input_by_id(wd,"username","s7799653")
input_by_id(wd,"password","songjianxin521..")
e_click_by_css(wd,".logging")
#WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,u" selenium webdriver定位不到元素的五种原因及解决办法（51testing"))).click()
#ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
#WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,u"軟件安全測試的測試用例格式參考"))).click()
e_click_by_partial_link(wd,u'軟件安全測試的測試用例格式參考')
e_click_by_id(wd,'btnDigg')
print(WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[3]/div[1]/div/div[2]/div[7]/dl[1]/dd'))).text)
Brower_quit(wd)
