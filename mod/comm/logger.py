#coding=utf-8

import time,os,logging
#获取当前父目录的路径
cur_path = os.path.dirname(os.path.dirname(__file__))
#当前父目录下的selenium_log的目录
log_file = os.path.join(cur_path, "selenium_log")
file_steam = False
if not os.path.exists(log_file):
    os.mkdir(log_file)
    file_steam = True
class Log:
    def __init__(self):
        '''文件命名与存储位置'''
        self.logname = os.path.join(log_file,str('%s.log' %time.strftime('%Y_%m_%d %H.%m.%S')))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        '''创建事务'''
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
    def __console(self, level, message):
        #创建filehandler，用于写在本地
        fh = logging.FileHandler(self.logname,'a')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        #创建一个SteamHandler，用户输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG) #定义日志等级
        ch.setFormatter(self.formatter) #设置事务
        self.logger.addHandler(ch)#将日志处理程序记录到记录器

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        #防止日志重复
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()
    def debug(self,message):
        self.__console('debug',message)
    def info(self,message):
        self.__console('info',message)
    def warning(self,message):
        self.__console('warning',message)
    def error(self,message):
        self.__console('error',message)
if __name__ == '__main__':
    log = Log()
    log.info('----start test ----')
    log.info('hello word')
    log.warning('----测试结束')