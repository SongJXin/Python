#coding=utf-8
from click_and_input import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
wd=webdriver.Chrome()
open_URL(wd,"http://www.baidu.com")
input_by_id(wd,"kw","福哥杂记 CSDN")
e_click_by_id(wd,"su")
#wd.find_element_by_link_text(u"福哥杂记,软件生命周期中的攻防博弈 - CSDN博客").click()
#e_click_by_link(wd,u"福哥杂记,软件生命周期中的攻防博弈 - CSDN博客")
e_click_by_partial_link(wd,u"软件生命周期中的攻防博弈")

