import random
import time
# import os


"""
大乐透开奖日：
周一 周三 周六
选号原则：
01---35 选 5 
01---12 选 2
双色球开奖日：
周二 周四 周日
01---33 选 6 红球
01---16 选 1 篮球
"""

def get_time():
    time_stamp = time.time()
    curent_time = time.asctime(time.localtime(time_stamp))
    return curent_time
"""
@:return:
Sat Oct 5 14:56:25 2019
星期 月份 日期 具体时间 年份
"""

def get_a_random_number(end_int, start_int = 1):
    return random.randint(start_int,end_int)
"""
@:param
@:func 设置随机数范围
end_int 截止范围
start_int 起始范围
@:return
随机数
"""

def get_the_num_lst(count = 5,range = 35):
    lst = []
    while len(lst) < count:
        tem_num = get_a_random_number(range)
        if tem_num not in lst:
            lst.append(tem_num)
    lst.sort(reverse=False)
    return str(lst)
"""
@:return
返回随机数数组
@:param：
count:数组中元素个数
range:随机数截止范围
"""

def time_info_lst():
    time_lst =str(get_time()).split(" ")
    return time_lst
"""
@:return
以列表的形式返回时间信息：
[Sat,Oct,day,time,year]
"""

def daletou():
    first_five_lst = get_the_num_lst()
    last_two_lst = get_the_num_lst(2, 12)
    return first_five_lst,last_two_lst
"""
:return:
返回值[0],前五位
返回值[1],后两位
"""
def shuangseqiu():
    red_ball_lst = get_the_num_lst(6,33)
    blue_ball_lst = get_the_num_lst(1,16)
    return red_ball_lst,blue_ball_lst
"""
:return
返回值[0]：红球
返回值[1]：蓝球
"""
def dlt_or_ssq():
    """
    大乐透开奖日：
    周一 周三 周六
    """
    dlt_data = ["mon","wed","sat"]
    data = str(time_info_lst()[0]).lower()
    if data == "fri":
        return "今天不开奖","0"
    elif data in dlt_data:
        return "大乐透开奖日！","1"
    else:
        return "双色球开奖日！","2"

"""
判断开奖的是大乐透还是双色球
"""
def file_name_combin():
    time_stamt = str(time_info_lst()[1]) + " " + str(time_info_lst()[3])
    # print(time_info_lst())
    if dlt_or_ssq()[1] == "1":
        return "DLT " + time_stamt + ".text"
    elif dlt_or_ssq()[1] == "2":
        return "SSQ " + time_stamt + ".text"
    else:
        return "休息" + time_stamt + ".text"
"""
文件路径及名称
"""

def text_words():
    text_word = """今天是{}\n\n第一组数字：{}\n第二组数字：{}\n生成时间：{}"""
    dltorssq = dlt_or_ssq()
    time = get_time()
    text_param_1 = dltorssq[0]
    if dltorssq[1] == "1":
        text_param = daletou()
    elif dltorssq[1] == "2":

        text_param = shuangseqiu()
    else:
        return "今天{}!\n\n".format(text_param_1)
    return text_word.format(text_param_1,text_param[0],text_param[1],time)

if __name__ == "__main__":
    text = text_words()
    path = file_name_combin()
    with open(path, "w+") as f:
        f.write(text)
