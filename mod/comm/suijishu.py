#coding:utf-8

import random

def generate_verification_code():
    ''' 随机生成6位的验证码 '''
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # A-Z
        code_list.append(chr(i))
    for i in range(97, 123): # a-z
        code_list.append(chr(i))

    myslice = random.sample(code_list, 20)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    # print code_list
    # print type(myslice)
    return verification_code

def generate_verification_code2():
    ''' 随机生成6位的验证码 '''
    code_list = []
    for i in range(2):
        random_num = random.randint(0, 9) # 随机生成0-9的数字
        # 利用random.randint()函数生成一个随机整数a，使得65<=a<=90
        # 对应从“A”到“Z”的ASCII码
        a = random.randint(65, 90)
        b = random.randint(97, 122)
        random_uppercase_letter = chr(a)
        random_lowercase_letter = chr(b)

        code_list.append(str(random_num))
        code_list.append(random_uppercase_letter)
        code_list.append(random_lowercase_letter)
    print code_list
    verification_code = ''.join(code_list)
    return verification_code
def get_phone_num1():
    phone_num = ['187','132']
    #手机号区域
    random_num = choice(phone_num)
    code_list = []
    # for i in range(8):
    #     code_list.append(str(random.randrange(0,9)))
    for i in range(10):
        code_list.append(str(i))
    myslice =random.sample(code_list,8)
    code = ''.join(myslice)
    result = random_num+code
    print result
def get_phone_num2(phone_name):
    #电信
    phone_DX = ['133','153','177','180','181','189']
    #联通
    phone_LT = ['130','131','132','155','156','185','186','145','176']
    #移动
    phone_YD = ['134','135','136','137','138','139','147','150','151','152','157','158','159','178','182','183','184','187','188']
    #手机号区域
    if  phone_name == '电信':
        random_num = choice(phone_DX)
    elif phone_name == '联通':
        random_num =choice(phone_LT)
    elif phone_name == '移动':
        random_num = choice(phone_YD)
    else:
        return  'input parameter'
    code_list = []
    for i in range(8):
        code_list.append(str(random.randrange(0,9)))
    code = ''.join(code_list)
    result = random_num+code
    print result
if __name__ == '__main__':
    # code = generate_verification_code()
    # code2 = generate_verification_code2()
    # print code
    # print code2
    get_phone_num1()
    get_phone_num2('联通')