import csv
import requests
import threading
import json


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
class get_account_session:
    def __init__(self,act_id):
        self.act = act_id

    def read_text(self, type, rows=None):
        if type == "read":
            with open("user_id.txt", "r", encoding="utf-8") as r:
                count_data = r.readlines()
                return count_data
        if type == "write":
            if rows == None:
                return False
            with open("jemter_01.csv", "a+", encoding='utf-8', newline="") as w:
                c = csv.writer(w)
                c.writerows(rows)
            return "写入完成"
    def common_req(self,method,url,body,header=None):
        if method == "get":
            headers = header
            if headers:
                r = requests.request('get',url,params=body,headers = header)
            else:
                r = requests.request('get',url,params=body)
            return r
        if method == 'post':
            headers = header
            if not headers:
                return False
            try:
                r = requests.request('post',url,json=body,timeout=6)
                return r
            except Exception as e:
                print(e)
                return False
    def common_url(self,dict_name):
        url_dict={
            "auto_login":'',
            "get-user-info":''
        }
        return url_dict[dict_name]
    def get_session(self, user_id):
        '''
        获取session_id
        '''
        # 请求结果返回
        headers = {
            "grpc-metadata-orgcode": ""
        }
        body = {
            "user_id": user_id
        }
        session_id = self.common_req(method='post',url=self.common_url('auto_login'),header=headers,body=body)
        return session_id
    def get_user_info(self, cookie, user_id):
        head = {
            "cookie": ""
        }
        param = {
            "user_id":"",
            "orgcode":""
        }
        
        user_info =self.common_req(method='get',url=self.common_url('get-user-info'),header=head,body=param)
        if user_info is False:
            return False
        for i in user_info.json()['data']['data']:
            if i['code'] == "mobile":
                return i['value']

    def register_agent(self, cookie,user_id,phone):
        url = ""
        head = {
            "cookie": ""
        }
        body = {
            "user_info": {
                "user_id": "",
                "user_name": "",
                "user_avatar": "",
                "user_phone": "
            },
            "spread_context": "",
            "activity_id": ""
        }
        r = requests.post(url, headers=head,json=body,timeout=1).json()
        return r['data']['ciphertext']
    def SaveRegisterInviteDetail(self,user_id,phone):
        url = ''
        body = {}
        url2 = ''
        r = requests.post(url, json=body)
        r2 = requests.post(url2, json=body).json()

        return r2

    def rep_restult(self, id):
        '''
        :param id 用户user_id
        :param act_id 活动id
        :return 返回数组 包含用户id，用户sessionid，租户信息，用户手机号码，活动id
        '''
        try:
            r = self.get_session(id).json()  # session_id
            if r == False:
                return False
            user_info = self.get_user_info(r['session_id'], id)  # 用户信息
            if user_info == "":
                return False
            inv = self.SaveRegisterInviteDetail(id,user_info)

            return [user_info,self.act,inv['ciphertext']['p'],inv['ciphertext']['k'],inv['ciphertext']['t']]
        except Exception as e:
            r = self.get_session(id)
            if r.status_code == 200:
                print(str(e) + '\n' + str(r.content))
                return False
            if r.status_code in (300, 500):
                print(id + '; status_code: ' + str(r.status_code))
                return False

    def data_logic(self, t_num: int):
        '''
        :param t_num 每组的list数量是20个
        '''
        r_date = self.read_text(type="read")
        statistic = len(r_date)
        d = 0  # 用于统计
        df = t_num  # 用于统计
        data_count = []
        while d < statistic:
            n = []
            for i in r_date[d:df]:
                dl_i = i.strip('\n')
                if dl_i == 'user_id':
                    continue
                if len(dl_i) >= 19:
                    n.append(dl_i)
            d += t_num
            df += t_num
            data_count.append(n)
        return data_count

    def thread_run(self, threadNum, act_id):
        if act_id == "":
            return False
        thread = []
        res = []
        for i in threadNum:
            t = MyThread(self.rep_restult, args=(i, act_id,))
            thread.append(t)
        for t in thread:
            t.setDaemon(True)
            t.start()
        for t in thread:
            t.join()
            try:
                if isinstance(t.get_result(), bool):
                    print("False Data: " + str(t.get_result()))
                    continue
                res.append(tuple(t.get_result()))
            except Exception as e:
                return False
        return res


if __name__ == '__main__':
    import time
    import os
    thread_num = 10
    file = 'jemter_01.csv'
    act_id = ""
    if os.path.isfile(file):
        os.remove(file)
    print(time.time())
    s = data_logic(thread_num)
    list_dta = s.data_logic(int(thread_num))
    for i in list_dta:
        dx = s.thread_run(i, act_id)
        if act_id == "":
            print("")
            break
        if dx == False:
            continue
        s.read_text("write", dx)
        # print("pass")
    print("pass")
    print(time.time())
