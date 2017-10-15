from selenium import webdriver

wd=webdriver.Chrome()
wd.get('https://www.baidu.com/')
wd.find_element_by_css_selector("#kw").send_keys(u'福哥杂技 CSDN')

wd.find_element_by_css_selector('#su').click()
#wd.quit()
