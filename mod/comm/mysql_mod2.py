#coding:utf-8

import MySQLdb
import sys
# from mod_config import *
# from logger import Log
reload(sys)
sys.setdefaultencoding('utf-8')

# log = Log()
class MysqldbHelper:
    #获取数据库连接
    def __init__(self):
        self.conn =MysqldbHelper.__getCon()
        self.cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    @staticmethod
    def __getCon():
        try:
            conn=MySQLdb.connect(host="locathost",
                                 user="username",
                                 passwd="pw",
                                 db="db",
                                 port=3306,
                                 charset="utf8")
            return conn
        except MySQLdb.Error,e:
            print "Mysqldb Error:%s" %e
    #查询方法，使用con.cursor(MySQLdb.cursors.DictCursor),返回结果为字典
    def Getall(self,sql,param = None):#手动输入sql语句
        '''
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组）
        @return: result list(字典对象)/boolean 查询到的结果集
        '''
        # cur= self.conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            if param == None:
                rep_sql = self.cur.execute(sql)
            else:
                rep_sql = self.cur.execute(sql,param)
            if rep_sql > 0:
                result = self.cur.fetchall()
            else:
                result = False
            return result
        except MySQLdb.Error,e:
            print "Mysqldb Error:%s" %e
        finally:
            self.cur.close()
    def Getone(self,sql,param = None):
        '''
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表），单个查询返回列表
        @return: result list/boolean 查询到的结果集
        '''
        cur= self.conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            if param == None:
                rep_sql = cur.execute(sql)
            else:
                rep_sql = cur.execute(sql,param)
            if rep_sql > 0:
                result = cur.fetchone()
            else:
                result = False
            return result
        except MySQLdb.Error,e:
            # log.info("Mysqldb Error:%s" %e)
            pass
        finally:
            cur.close()
    def GetNum(self,sql, num, param = None):
        '''
        @summary: 执行查询，并取出num条结果
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组）
        @return: result list/boolean 查询到的结果集,返回tuple
        '''
        cur= self.conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            if param == None:
                rep_sql = cur.execute(sql)
            else:
                rep_sql = cur.execute(sql,param)
            if rep_sql > 0:
                result = cur.fetchmany(num)
            else:
                result = False
            return result
        except MySQLdb.Error,e:
            pass
            # log.info("Mysqldb Error:%s" %e)
        finally:
            cur.close()
    #带参数的更新方法,eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
    def InsertOne(self,sql,value):
        '''
        :param sql: 语法 inster into tables_name(a,b,c)vales(%s,%s,%s)
        :param value: %s的参数
        :return:
        '''
        cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cur.execute(sql,value)
            cur.commit()
            return self.__getInsertId()
        except MySQLdb.Error,e:
            print "Mysql Error %s"%e
            cur.rollback()
        finally:
            cur.close()
    #使用executemany插入时，数量量超过1M时，会报错，因为mysql中设置了最大的是1M的数据量；这时就需要去修改mysql的设置
    def IsertMany(self,values,sql):
        '''
        :param values:  %s参数,必须是tuple的类型
        :param sql: mysql语法格式（insert into tables_name(a,b,c) values(%s,%s,%s)
        :return: 插入的速度是execute的十倍快
        eg:
        for i in range(2):
            values.append((i,i))
        print len(values)
        '''
        cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            count = cur.executemany(sql,values)
            cur.commit()
            return count
        except MySQLdb.Error,e:
            # log.info("Mysql Error: %s"%e)
            cur.rollback()
        finally:
            cur.close()
    def __getInsertId(self):
        """
        获取当前连接最后一次插入操作生成的id,如果没有则为０
        """
        self.conn.execute("SELECT @@IDENTITY AS id")
        result = self.conn.fetchall()
        return result[0]['id']
    def updateByParam(self,sql,params = None):
        '''cursor.execute("SELECT * FROM t1 WHERE id = %s", (5,))'''
        try:
            cur=self.conn.cursor(MySQLdb.cursors.DictCursor)
            if params == None:
                count = cur.execute(sql)
            else:
                count = cur.execute(sql,params)
            cur.commit()
            return count
        except MySQLdb.Error,e:
            cur.rollback()
            print "Mysqldb Error:%s" %e
        finally:
            cur.close()
    def delete_information(self,sql,params = None):
        cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            if  params == None:
                count =cur.execute(sql)
            elif type(params) == type(tuple()):
                count =cur.executemany(sql,params)
            else:
                #executemany必须是tuple的类型才可以使用
                count =cur.executemany(sql,params)
            cur.commit()
            return  count
        except MySQLdb.Error,e:
            cur.rollback()
            print "Mysql Error %s" %e
        finally:
            cur.close()
if __name__ == "__main__":
    a = MysqldbHelper()
    # sql="select * from phoneuser WHERE account = %s and alias = %s"
    sql="select * from camera WHERE cid = %s"
    # print sql
    par = ('290200000011')
    fd = a.Getall(sql,par)
    print fd


    #循环插入的例子
     # fd=a.select(sql)
    # value=[1,'hi rollen']
    # cur.execute('insert into test values(%s,%s)',value)
    #
    # values=[]
    # for i in range(20):
    #     values.append((i,'hi rollen'+str(i)))
    #
    # cur.executemany('insert into test values(%s,%s)',values)
    #
    # cur.execute('update test set info="I am rollen" where id=3')
    #
    # conn.commit()
    # cur.close()
    # conn.close()