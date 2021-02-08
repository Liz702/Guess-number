import random
min = input('请输入猜测范围的最小值： ')
max = input('请输入猜测范围的最大值： ')
min = int(min)
max = int(max)
r = random.randint(min, max)
i = 0
while True:
    num = input('请输入您猜测的数字： ')
    num = int(num)
    i = i + 1
    print('您猜了', i, '次')
    if num == r:
    	print('您猜对了，恭喜')
    	break
    elif num > r:
    	print('比结果大')
    else:
    	print('比结果小')