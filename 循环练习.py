#计算1~100的和

# i = 1
# num = 0
# while i <= 100:
#     num += i
#     i += 1
# print(num)

#计算1~100偶数的累加和

# i = 1
# num = 0
# while i <= 100:
#     if i % 2 == 0:
#      num += i
#     i += 1
# print('偶数和为%d' %num)

# i = 2
# num = 0
# while i <= 100:
#     if i % 2 == 0:
#      num += i
#     i += 2
# print('偶数和为%d' %num)

#循环嵌套

i = 1
while i <= 5:
    print('%d' %i)
    num = 0
    while num < 3:
        num += 1
        print('233')
    i += 1