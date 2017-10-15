from selenium import webdriver

wd=webdriver.Chrome()
wd.get('https://www.baidu.com/')
wd.find_element_by_xpath(".//*[@id='kw']").send_keys(u'福哥杂技 CSDN')
wd.find_element_by_xpath(".//*[@id='su']").click()
wd.quit()

