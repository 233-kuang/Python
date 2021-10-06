import random

mora = eval(input('请输入石头（1）剪刀（2）布（3）'))

computer = random.randint(1,3)#随机生存1~3数字

if mora == computer:
    print('平局')
elif (mora ==1 and computer == 2) or ( mora == 2 and computer == 3) or ( mora == 3 and computer == 1):
    print('玩家胜')
else:
    print('你输了')
