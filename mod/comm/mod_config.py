#coding:utf8
import os,json,logger
import MySQLdb

log = logger.Log()
class DB_Confg():
    '''读取mysql的json配置文件'''
    cur_path = os.path.dirname(os.path.realpath(__file__))
    try:
        if not os.path.exists(cur_path + "\\" + "peizhi"):
            log.info("缺少配置文件")
        with open(cur_path + "\\" + "peizhi",'r') as f:
            db = json.load(f)
    except Exception as e:
        print "Error %s" %e
    @staticmethod
    def User_sql():
        return DB_Confg.db["mysql"]["user"]

    @staticmethod
    def Password_Sql():
        return DB_Confg.db["mysql"]["password"]

    @staticmethod
    def Host_Sql():
        return DB_Confg.db["mysql"]["hosts"]

    @staticmethod
    def Port_Sql():
        return DB_Confg.db["mysql"]["port"]

    @staticmethod
    def Dbname_Sql():
        return DB_Confg.db["mysql"]["dbname"]

    @staticmethod
    def Charset_Sql():
        return DB_Confg.db["mysql"]["chart"]

class Redis_DB():
    '''读取mysql的json配置文件'''
    cur_path = os.path.dirname(os.path.realpath(__file__))
    try:
        if not os.path.exists(cur_path + "\\" + "peizhi"):
            log.info("缺少配置文件")
        with open(cur_path + "\\" + "peizhi",'r') as f:
            db = json.load(f)
    except Exception as e:
        print "Error %s" %e
    @staticmethod
    def Host_R():
        return Redis_DB.db["redis"]["host"]\

    @staticmethod
    def User_R():
        return Redis_DB.db["redis"]["user"]

    @staticmethod
    def Pwd_R():
        return Redis_DB.db["redis"]["password"]

    @staticmethod
    def Port_R():
        return Redis_DB.db["redis"]["port"]

if __name__ == "__main__":
    a = DB_Confg
    conn=MySQLdb.connect(host=a.Host_Sql(),
                     user=a.User_sql(),
                     passwd=a.Password_Sql(),
                     db=a.Dbname_Sql(),
                     port=int(a.Port_Sql()),
                     charset=a.Charset_Sql())
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    connect1 = cur.execute("select * from phoneuser WHERE  account = '%s'" %'testmdm1@126.com')
    a = cur.fetchone()
    print a
    cur.close()