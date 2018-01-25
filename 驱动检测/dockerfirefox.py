#coding=utf-8
from  selenium import webdriver
firefox_capabilities ={
    "browserName": "firefox",
    "version": "47.0",
    "platform": "ANY",
    "javascriptEnabled": True,
    "marionette": True,
}
browser=webdriver.Remote("http://10.10.8.1：4444/wd/hub",desired_capabilities=firefox_capabilities)
browser.get("http://www.baidu.com")
browser.get_screenshot_as_file("baidu.png")
browser.close()
