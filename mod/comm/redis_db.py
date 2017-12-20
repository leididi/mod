#coding:utf-8
import redis
from mod_config import Redis_DB
import msgpack

class Redis_Mod():
    def __init__(self):
        self.conn = Redis_Mod.__getCon()
    @staticmethod
    def __getCon():
        try:
            conn = redis.Redis(host= Redis_DB.Host_R(),
                               port= Redis_DB.Port_R(),
                               password= Redis_DB.Pwd_R(),
                               db= 0)
            return conn
        except Exception as e:
            print "Redis Error: %s"%e
    def Keys_List(self,value=None):
        if value == None or value == "":
            return "请输入需要搜索的内容"
        else:
            count = self.conn.keys(value)
            return count
    def Get_info(self,value):
        if value == None or value == "":
            return "请输入get内容"
        else:
            count = self.conn.get(value)
            return msgpack.unpackb(count)
    def Del_info(self,value):
         if value == None or value == "":
             return "请输入删除的内容"
         else:
            count = self.conn.delete(value)
            return  count
# if __name__ == "__main__":
#     a = Redis_Mod()
#     b =a.KeysGet("*")
#     print type(b)