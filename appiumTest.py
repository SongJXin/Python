#coding=utf-8
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'  
desired_caps['platformVersion'] = '6.0'  
desired_caps['deviceName'] = 'MTP'  
desired_caps['appPackage'] = 'com.android.calculator2'  
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.install_app("C:\\Users\\songjl\\Desktop\\tim.apk")
#driver.find_element_by_id('com.android.calculator2:id/digit2').click()
driver.quit()
print('over')
