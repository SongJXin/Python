#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
#  PAGE-DOWN
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#open web page
def open_URL(wd,url):
    wd.get(url)


#find element and click by link text
def e_click_by_link(wd,str1):
    #element=WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT,str1)))
    while True:
        try:
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT,str1))).click()
            break
        except selenium.common.exceptions.TimeoutException :
            print("not search element link = ",str1)
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)
            

#find element and click by partial link text
def e_click_by_partial_link(wd,str1):
    #element=WebDriverWait(wd, 20, 0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, str1)))
    while True:
        try:
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, str1))).click()
            break
        except selenium.common.exceptions.TimeoutException :
            print("not search element partial_link =%s "%(str1))
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)

            
#find element and click by id
def e_click_by_id(wd,str1):
    #element=WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.ID,str1)))
    while True:
        try:
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.ID,str1))).click()
            break
        except selenium.common.exceptions.TimeoutException :
            print("not search element id = %s"%(str1))
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)

            
#find element and click by xpath
def e_click_by_xpath(wd,str1):
    #element=WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,str1)))
    while True:
        try:
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,str1))).click()
            break
        except selenium.common.exceptions.TimeoutException :
            print("not search element xpath = ",str1)
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)

            
#find element and click by css
def e_click_by_css(wd,str1):
   # element=WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,str1)))
    while True:
        try:
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,str1))).click()
            break
        except selenium.common.exceptions.TimeoutException :
            print("not search element css = ",str1)
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)

            
#exit brower but sleep 10s before it
def Brower_quit(wd):
    wd.quit()

    
#find element and input by id
def input_by_id(wd,id1,str1):
    #element=WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.ID,id1)))
    while True:
        try:
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.ID,id1))).clear()
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.ID,id1))).send_keys(str1)
            break
        except selenium.common.exceptions.TimeoutException :
            print("not search element id = ",id1)
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)


#find element and input by css
def input_by_css(wd,css,str1):
    #element=WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,css)))
    while True:
        try:
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,css))).clear()
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,css))).send_keys(str1)
            break
        except selenium.common.exceptions.TimeoutException :
            print("not search element css = ",css)
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)


#find element and input by xpath
def input_by_xpath(wd,xpath,str1):
    #element= WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,xpath)))
    while True:
        try:
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,xpath))).clear()
            WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,xpath))).send_keys(str1)
            break
        except selenium.common.exceptions.TimeoutException :
            print("not search element xpat = ",xpath)
        except Exception as err:
            ActionChains(wd).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)


#judge element is exist
def is_element_exist(wd,link):
    s=WebDriverWait(wd, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT,link)))
    if len(s)==0:
        return False
    else:
        return True
    
#switch tab page
def switch_tab_page(wd):
    now_handle=wd.current_window_handle
    all_handles =wd.window_handles
    for handle in all_handles:
        if handle!=now_handle:
            wd.switch_to.window(handle)
    return wd
