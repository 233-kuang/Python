score = int (input('请输入分数'))
if score >= 90:
    print('分数大于90你很优秀')
elif 80 <= score < 90:
    print('分数大于80，良好')
elif 60 <= score < 80:
    print('你的分数大于60，一般')
else:
    print('分数小于60不及格')