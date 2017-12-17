#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait
from comm.logger import Log
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()


def browser(browser = 'Chrome'):
    '''
    打开浏览器，"Firefox","Chrome","ie","phantomjs"
    '''
    try:
        if browser == "firefox":
            driver = webdriver.Firefox()
            log.info('start Firefox')
            return driver
        elif browser == "Chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("start-maximized")
            driver = webdriver.Chrome(chrome_options=chrome_options)
            log.info('start Chrome')
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            log.info('start IE')
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            log.info('start PhantomJS')
            return driver
        else:
            print ("Not found this browser,Your can enter firefox,Chrome,phantomjs,ie")
    except Exception as msg:
        print "%s" %msg

class yoyo(object):
    '''基于原生的selenium框架做二次封装'''
    def __init__(self,driver):
        """启动参数化，默认启动firefox"""
        self.driver = driver
    def open(self,url,t= '',timeout = 10):
        """
        使用get打开URL后，最大化窗口，判断title符合预期
        Usage：
        driver = yoyo(driver)
        driver.open(url,t='')
        """
        #使用chrome是62版本所以maximize_window无法将浏览器放大。而导致报错，增加判断；如果为chrome浏览器就不使用maximize_window；
        if "chrome" in str(self.driver):
            self.driver.implicitly_wait(30)
            self.driver.get(url)
        else:
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.driver.get(url)
        try:
            WebDriverWait(self.driver,timeout,1).until(EC.title_contains(t))
        except TimeoutException:
            print ("open %s title error"%url)
        except Exception as msg:
            print ("Error:%s"%msg)

    def find_element(self,locator,timeout = 10):
        '''
        定位元素，参数locator是元祖类型
        Usgae：
        locator = （"id","xxx")
        driver.find_element(locator)
        '''
        element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self,locator,timeout=10):
        '''
        定位一组元素
        '''
        elements =WebDriverWait(self.driver,timeout,1).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self,locator):
        '''
        点击操作
        Ugae：
        locator = ("id", "xxx")
        driver.click()
        '''
        element = self.find_element(locator)
        element.click()

    def send_keys(self,locator,text):
        '''
        发送文本，清空后输入
        Ugae：
        locator = ("id", "xxxx")
        driver.send_keys(locator,text)
        '''
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self,locator,text,timeout =10):
        '''
        判断文本在元素里,没定位到元素返回False，定位到返回判断结果布尔值
        result = driver.text_in_element(locator,text)
        '''
        try:
            result =WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))
        except TimeoutException:
            print "元素没定位到 :" + str(locator)
        else:
            return result
    def is_text_in_value(self,locator,value,timeout=10):
        '''
        判断元素的value的值，没定位到元素返回False，定位到返回判断结果布尔值
        result = driver.text_in_element(locator,text)
        '''
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(locator,value))
        except TimeoutException:
            print "元素没定位到 ：" + str(locator)
        else:
            return result

    def is_title_contains(self,title,timeout = 10):
            '''判断title包含'''
            result = WebDriverWait(self.driver,timeout,1).until(EC.title_contains(title))

            return result

    def is_select(self,locator,timeout = 10):
            '''判断元素被选中，返回布尔值'''
            result = WebDriverWait(self.driver,timeout,1).until(EC.element_located_to_be_selected(locator))
            return result

    def is_selected_be(self,locator,selected = True,timeout = 10):
            '''判断元素的状态，selected是期望的参数true/False'''
            result = WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(locator,selected))
            return result

    def is_alert_present(self,timeout=10):
            '''判断页面是否有alert，
            有返回alert（注意这里是返回alert，不是True）
            没有返回False'''
            result = WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())
            return result

    def is_visibility(self,locator,timeout = 10):
            '''元素可见返回本身，不可见返回False'''
            result = WebDriverWait(self.driver,timeout,1).until(EC.visibility_of_element_located(locator))
            return result

    def is_invisibility(self,locator,timeout=10):
            '''元素可见返回本身，不可见返回True,没找到元素也返回True'''
            result = WebDriverWait(self.driver,timeout,1).until(EC.invisibility_of_element_located(locator))
            return result

    def is_clickable(self,locator,timeout =10):
            '''元素可以点击is_enabled返回本身，不可点击返回False'''
            result =WebDriverWait(self.driver,timeout,1).until(EC.element_to_be_clickable(locator))
            return result

    def move_to_element(self,locator):
            '''鼠标悬停操作
            Usage:
            locator = ("id","xxx")
            driver.move_to_element(locator)
            '''
            element = self.find_element(locator)
            ActionChains(self.drver).move_to_element((element)).perform()

    def back(self):
            '''
            back to old window
            Uage:
            driver.back()
            '''

            self.driver.back()

    def forward(self):
            '''
            Forward to old window
            Uage:
            driver.forward
            '''
            self.driver.forward()

    def close(self):
            '''
            Close the windows.
            Uages:
            driver.close()
            '''
            self.driver.close()

    def quit(self):
            '''
             Quit the driver Close all the windows
            driver.quit()
            '''
            self.driver.quit()

    def get_text(self,locator):
            '''获取text'''
            element = self.find_element(locator)
            return element.text

    def get_title(self):
            '''获取title'''
            return self.driver.title

    def get_attribute(self,locator,name):
            '''获取属性'''
            element = self.find_element(locator)
            return element.get_attribute(name)

    def js_exeute(self,js):
            '''执行js'''
            return  self.driver.execute_script(js)

    def js_focus_element(self,locator):
            '''聚焦元素'''
            target = self.find_element(locator)
            self.driver.execute_script("argument[0].scrollIntoView();",target)

    def js_scoll_top(self):
            '''滚动到顶部'''
            js ="window.scrollTo(0,0)"
            self.driver.execute_script(js)

    def js_scoll_end(self):
            "滚动到底部"
            js ="window.scrollTo(0,document.body.scrollHeight)"
            self.driver.execute_script(js)

    def select_by_index(self,locator,index):
            '''通过索引，index是索引第几个，从0开始'''
            element = self.find_element(locator)
            Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
            '''听过value属性'''
            element =self.find_element(locator)
            Select(element).select_by_value(value)
    def select_by_text(self,locator,text):
            '''通过文本值定位'''
            element = self.find_element(locator)
            Select(element).select_by_value(text)
if __name__ == "__main__":
    #if 下面的代码都是测试调试的代码，自测内容
    driver = browser("Chrome")
    driver_n = yoyo(driver)#返回类的实例：打开浏览器
    driver_n.open("http://www.cnblogs.com/yoyoketang/")# 打开url，顺便判断打开的页面对不对
    input_loc =("id","kw")
    print driver_n.get_title()
    # el = driver_n.find_element(input_loc)
    # driver_n.send_keys(input_loc, "yoyo")
    # button_loc = ("id", "su")
    # driver_n.click(button_loc)
    # print driver_n.text_in_element(("name", "tj_trmap"), "地图")
    # set_loc = ("link text", "设置")
    # driver_n.move_to_element(set_loc)
    driver.quit()
