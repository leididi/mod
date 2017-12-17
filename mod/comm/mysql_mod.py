#coding:utf-8

import MySQLdb
import sys
from mod_config import *
reload(sys)
sys.setdefaultencoding('utf-8')
1
class MysqldbHelper:
    #获取数据库连接
    def getCon(self):
        try:
            conn=MySQLdb.connect(host=DB_Confg.Host_Sql(),
                                 user=DB_Confg.User_sql(),
                                 passwd=DB_Confg.Password_Sql(),
                                 db=DB_Confg.Dbname_Sql(),
                                 port=DB_Confg.Port_Sql(),
                                 charset=DB_Confg.Charset_Sql())
            return conn
        except MySQLdb.Error,e:
            print "Mysqldb Error:%s" %e
    #查询方法，使用con.cursor(MySQLdb.cursors.DictCursor),返回结果为字典
    def input_select(self,sql):#手动输入sql语句
        try:
            con=self.getCon()
            cur=con.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(sql)
            fc=cur.fetchone()
            return fc
        except MySQLdb.Error,e:
            print "Mysqldb Error:%s" %e
        finally:
            cur.close()
    def parameter_select(self,sql,params):
        try:
            con = self.getCon()
            cur = con.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(sql,params)
            fc = cur.fetchall()
            return fc
        except MySQLdb.Error,e:
            print "Mysql Error %s" %e
        finally:
            cur.close()
    #带参数的更新方法,eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
    def updateByParam(self,sql,params):
        '''cursor.execute("SELECT * FROM t1 WHERE id = %s", (5,))'''
        try:
            con=self.getCon()
            cur=con.cursor(MySQLdb.cursors.DictCursor)
            count=cur.execute(sql,params)
            con.commit()
            return count
        except MySQLdb.Error,e:
            con.rollback()
            print "Mysqldb Error:%s" %e
        finally:
            cur.close()
            con.close()
    #不带参数的更新方法
    def update(self,sql):
        try:
            con=self.getCon()
            cur=con.cursor()
            count=cur.execute(sql)
            con.commit()
            return count
        except MySQLdb.Error,e:
            con.rollback()
            print "Mysqldb Error:%s" %e
        finally:
            cur.close()
            con.close()
    def circulation_update(self,sql,params,params1):
        '''多参数sql语句
        data = [
            ('Jane','555-001'),
            ('Joe', '555-001'),
            ('John', '555-003')
            ]
        stmt = "INSERT INTO employees (name, phone) VALUES ('%s','%s')"
        cursor.executemany(stmt, data)
        '''
        try:
            con = self.getCon()
            cur = con.cursor()
            values = []
            for i in range(1):
                values.append((params,params1))
            cur.executemany(sql,tuple(values))
            cur.commit()
        except MySQLdb.Error,e:
            cur.rollback()
            print "Mysql Error %d :%s" %(e.args[0],e.args[1])
    #删除数据
    def delete_information(self,sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            cur.execute(sql)
            cur.commit()
        except MySQLdb.Error,e:
            cur.rollback()
            print "Mysql Error %s" %e
        finally:
            cur.close()
    def delete_infor_param(self,sql,params):
        try:
            con = self.getCon()
            cur = con.cursor()
            cur.execute(sql,params)
            cur.commit()
        except MySQLdb.Error,e:
            cur.rollback()
            print "Mysql Error %s" %e
        finally:
            cur.close()

if __name__ == "__main__":
    a = MysqldbHelper()
    # sql="select * from phoneuser WHERE account = %s and alias = %s"
    # sql="select * from camera WHERE cid = '%s'" %290200000011
    # print sql
    # # par = ('testmdm1@126.com','rghvfgi')
    # fd = a.input_select("select * from camera WHERE cid = '%s'" %290200000011)
    # print fd

    # for row in fd:
    #     print row[""]


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
    values=[]
    for i in range(2):
        values.append((i,i))
    print len(values)