#coding=utf-8

from selenium import webdriver

wd=webdriver.Firefox()
wd.get('https://www.baidu.com/')
wd.find_element_by_id('kw').send_keys(u'福哥杂技 CSDN')

wd.find_element_by_id('su').click()
wd.quit()
