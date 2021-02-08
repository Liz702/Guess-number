import random
r = random.randint(1,100)
while True:
    num = input('请输入您猜测的数字： ')
    num = int(num)
    if num == r:
    	print('您猜对了，恭喜')
    	break
    elif num > r:
    	print('比结果大')
    else:
        print('比结果小')