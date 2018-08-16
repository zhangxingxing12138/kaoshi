class InputError(Exception):
    pass
with open('123.txt','r') as f:
    users = [i.replace('\n','').split('|') for i in f.readlines()]
    user_dict = {i[0]:i[1] for i in users}
    print(user_dict)
import re
def login(func):
    def wapper(file_name):
        username = input('username:')
        if re.match(r'[\u4e00-\u9fff]',username) is not None:
            raise InputError('不能输入中文')
        password = input('ppassword:')
        passwd = user_dict.get(username)
        if passwd is not None:
            if passwd == password:
                func(file_name)
            else:
                print('密码错误')
        else:
            print('没有找到这个用户')
    return wapper
import os
@login
def rm_file(file_name:str) -> bool:
    if os.path.exists(file_name):
        os.remove(file_name)
        return True
    else:
        return False
rm_file('1.py')
    
