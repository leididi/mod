import requests
import datetime
import time


def comm_req(body):
    url = ''
    header = {
        'Content-Type': 'application/json'
    }
    data = body
    r = requests.post(url, json=data, headers=header)
    return r


def wechat_rep(type_str):
    body = {
        "today": {
            "msgtype": "markdown",
            "markdown": {
                "content": "# 开始播报"
            },
            "mentioned_list": [
                "@all"
            ]
        },
        "sleep": {
            "msgtype": "markdown",
            "markdown": {
                "content": "# 已坐40分钟 屁股坐热，肩膀硬了，脖子痛了，赘肉多了\n\n  来站站走走看看；运动啦啦啦啦啦"
            },
            "mentioned_list": [
                "@all"
            ]
        },
        "Go_off_work": {
            "msgtype": "markdown",
            "markdown": {
                "content": "到点了，该加班的加班，该下班下班的下班"
            },
            "mentioned_list": [
                "@all"
            ]
        }
    }
    if type_str == "sleep":
        comm_req(body[type_str])
        return
    if type_str == "Go_off_work":
        comm_req(body[type_str])
        return
    if type_str == "today":
        comm_req(body[type_str])
        return


def time_logic():
    now = datetime.date.today()
    eig_m = now.strftime("%Y-%m-%d 09:00:00")
    elevery_m = now.strftime("%Y-%m-%d 12:00:00")
    two_m = now.strftime("%Y-%m-%d 14:00:00")
    down_work = now.strftime("%Y-%m-%d 18:00:00")
    e_m = int(time.mktime(time.strptime(elevery_m, "%Y-%m-%d %H:%M:%S")))
    t_m = int(time.mktime(time.strptime(two_m, "%Y-%m-%d %H:%M:%S")))
    d_m = int(time.mktime(time.strptime(down_work, "%Y-%m-%d %H:%M:%S")))
    eg_m = int(time.mktime(time.strptime(eig_m, "%Y-%m-%d %H:%M:%S")))
    return e_m, t_m, d_m, eg_m


def while_logic(default_time, count_time: int):
    # 执行到这里的时间
    if default_time[0] <= count_time < default_time[1]:
        return "1"
    if default_time[3] <= count_time < default_time[0]:
        if count_time - 1 <= count_time <= count_time + 1:
            wechat_rep("sleep")
            return "0"
    if count_time < default_time[2]:
        if count_time - 1 <= count_time <= count_time + 1:
            wechat_rep("sleep")
            return "0"
    if count_time == default_time[2]:
        if count_time - 1 <= count_time <= count_time + 1:
            wechat_rep("Go_off_work")
            return "2"
    if count_time > default_time[2]:
        return "2"


def run_logic():
    default_time = time_logic()
    switch = "0"
    timekeeper = ""
    while True:
        count_time = int(time.time())  # 本次进入的时间
        if timekeeper == "":  # 记录为空时，走一遍查看结果
            # print("播报开始")
            wechat_rep("today")
            timekeeper = count_time + 2400
            # timekeeper = count_time + 1
        if switch == "1":
            print("中午休息时间")
            timekeeper = count_time + 7200
        if switch == "2":
            print("下班了")
            break
        if switch == "0" and int(timekeeper) - 1 <= count_time <= int(timekeeper) + 1:
            # print("间隔休息时间")
            switch = while_logic(default_time, count_time)
            timekeeper = count_time + 2400


if __name__ == "__main__":
    run_logic()
