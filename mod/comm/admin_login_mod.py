#coding:utf-8

from selenium import webdriver
import time,sys
from comm.logger import Log

reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()

class Login_admin:
    def __init__(self,driver):
        self.driver = driver
    def input_name(self,username):
        '''输入用户名'''
        self.driver.find_element_by_id('email').clear()
        self.driver.find_element_by_id("email").send_keys(username)
    def input_pwd(self,pwd):
        '''输入密码'''
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(pwd)
    def click_botton(self):
        '''点击登录'''
        self.driver.find_element_by_id('submit').click()

    def login(self,username,pwd):
        self.input_name(username)
        self.input_pwd(pwd)
        self.click_botton()
        admin_user = self.driver.find_element_by_id('userEmail').text
        try:
            assert admin_user == u'testmdm3@126.com'
            log.info("成功登录管理平台，开始执行下列用例")
        except AssertionError,e:
            log.info("不在登录界面，无法执行下一步用例操作: %s" %e)


