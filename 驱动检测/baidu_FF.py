#coding=utf-8

from selenium import webdriver
chrome_capabilities ={
    "browserName": "Firefox",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    # "marionette": True,
}
wd=webdriver.Remote("http://123.207.143.69:4444",desired_capabilities=chrome_capabilities)
wd.get('https://www.baidu.com/')
wd.find_element_by_id('kw').send_keys(u'哈哈')

wd.quit()
