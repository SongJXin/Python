#coding=utf-8

from selenium import webdriver
import time
#open firefox
wd=webdriver.Firefox()
#jump to baidu
wd.get('https://www.baidu.com/')
#search
wd.find_element_by_id('kw').send_keys(u'2017放假安排')
wd.find_element_by_id('su').click()
time.sleep(10)
#search
wd.find_element_by_id('kw').clear()
wd.find_element_by_id('kw').send_keys(u'福哥杂技 CSDN')
wd.find_element_by_id('su').click()
time.sleep(10)

#jump
wd.get('http://blog.csdn.net/otianye/article/details/78092614')
time.sleep(10)

#back
wd.back()
time.sleep(10)
wd.quit()
