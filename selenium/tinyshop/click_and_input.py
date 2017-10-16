#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
#web页面翻页 - 1 ：  PAGE-DOWN
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium

#open web page
def open_URL(wd,url):
    wd.get(url)


#find element and click by link text
def e_click_by_link(wd,str1):
    while True:
        try:
            wd.find_element(By.LINK_TEXT,str1).click()
            break
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()

            
#find element and click by id
def e_click_by_id(wd,str1):
    while True:
        try:
            wd.find_element_by_id(str1).click()
            break
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()

            
#find element and click by xpath
def e_click_by_xpath(wd,str1):
    while True:
        try:
            wd.find_element(By.XPATH,str1).click()
            break
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()

            
#find element and click by css
def e_click_by_css(wd,str1):
    while True:
        try:
            wd.find_element(By.CSS_SELECTOR,str1).click()
            break
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()

            
#exit brower but sleep 10s before it
def Brower_quit(wd):
    wd.quit()

    
#find element and input by id
def input_by_id(wd,id1,str1):
    while True:
        try:
            wd.find_element_by_id(id1).clear()
            wd.find_element_by_id(id1).send_keys(str1)
            break
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()


#find element and input by css
def input_by_css(wd,css,str1):
    while True:
        try:
            wd.find_element(By.CSS_SELECTOR,css).clear()
            wd.find_element(By.CSS_SELECTOR,css).send_keys(str1)
            break
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform() 


#find element and input by xpath
def input_by_xpath(wd,xpath,str1):
    while True:
        try:
            wd.find_element(By.XPATH,xpath).clear()
            wd.find_element(By.XPATH,xpath).send_keys(str1)
            break
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()   


#judge element is exist
def is_element_exist(wd,link):
    s=wd.find_elements(By.LINK_TEXT,link)
    if len(s)==0:
        return False
    else:
        return True
    
