tou = int(input('请输入头数：'))
jiao = int(input('请输入脚数：'))
jijiao = int(input('请输入鸡（单个腿少的东西）的腿（相当于腿）数：'))
tujiao = int(input('请输入兔（单个腿多的东西）的腿（相当于腿）数：'))
ji = 0
tu = 0
while True:
    tu = tou - ji
    if ji + tu == tou and ji * jijiao + tu * tujiao == jiao:
        break
    ji += 1
print('有'+str(ji)+'只鸡（单个腿少的东西），有'+str(tu)+'只兔（单个腿多的东西）。')