# -*- coding: cp936 -*-

from selenium import webdriver
import time

#webҳ�淭ҳ - 1 ��  PAGE-DOWN
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

start_url="http://news.baidu.com/"

#init browser obj
wd=webdriver.Chrome()   # chrome
wd.maximize_window()    # ������������

wd.get(start_url)  # open target web-site

time.sleep(10)
ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(10)
ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(10)
ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()

wd.quit()

