from selenium import webdriver

wd=webdriver.Remote("http://10.10.8.31:4444/wd/hub/",DesiredCapabilities.chrome())
wd.get('https://www.baidu.com/')
#wd.quit()
