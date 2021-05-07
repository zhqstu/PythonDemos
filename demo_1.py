# -*- coding: utf-8 -*-#
# ---------------------------
# Author:       STU
# Date:         2021/5/7
# Description:  随机生成六位数的验证码
# ---------------------------

import random


def generate_verification_code():
    """随机生成六位数验证码"""
    code_list = []                              # 生成list列表形式
    for i in range(10):
        code_list.append(str(i))                # 数字0-9
    for i in range(65, 91):
        code_list.append(chr(i))                # 字母A-Z
    for i in range(97, 123):
        code_list.append(chr(i))                # 字母a-z
# 从list中随机获取6个元素，作为一个片段返回
    myslice = random.sample(code_list, 6)
    verification_code = ''.join(myslice)        # list to string
    return verification_code


if __name__ == '__main__':
    code = generate_verification_code()
    print(code)
