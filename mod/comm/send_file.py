# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import SendKeys

dr = webdriver.Chrome()
dr.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = dr.find_element_by_id('file')
upload.click()
time.sleep(1)

SendKeys.SendKeys('C:\\Users\\c\\Desktop\\dolow\\apns.xml') # 发送文件地址
SendKeys.SendKeys("{ENTER}") # 发送回车键

print upload.get_attribute('value')
dr.quit()