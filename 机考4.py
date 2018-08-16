#def gen_str():
 #   return 'abcdefghijklmnopqrstuvwyz'
#print(gen_str())
#import random
#import os
#with open('user.txt','a+') as f:
 #   for i in range (200):
  #      s = gen_str()[:6]
   #     password = '0000'
    #    result = s+'_'+str(i)+'|'+password+'\n'
     #   f.write(result)
import random
import time
str_list = list(map(chr,range(97,123)))
s = [str(i) for i in range(10)]
#for i in range(200):
 #   random.shuffle(str_list)
    #print'',join(str_list[:6]))
  #  six = str_list[:6]
   # print(''.join(six))
    #random.shuffle(d)
    #print(''.join(d[:4]))
def first_func(s,count,length):
    result = [] 
    for i in range(count):
        random.shuffle(s)
        result.append(''.join(s[:length])) 
    return result
user_list = first_func(str_list,200,6)   
password = first_func(s,200,4)
with open ('123.txt','w') as f:
    for i in zip(user_list,password):
        print(i)
        f.write(str(i)+'\n')
