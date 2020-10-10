from time import time
from random import randint
from solver import solver

tims = []
lens = []
scrambles = []
cnt = 0
num = int(input('number of test cases: '))
for i in range(num):
    strt = time()
    test_cube = [randint(0, 11) for _ in range(14)]
    with open('log.txt', mode='a') as f:
        f.write(str(test_cube) + '\n')
    res = solver(test_cube)
    tim = time() - strt
    #print(i, len(res), 'moves', tim, 'sec')
    tims.append(tim)
    lens.append(len(res))
    scrambles.append(test_cube)
    cnt += 1
print(cnt, '/', num)
print('avg', sum(tims) / cnt, 'sec', 'max', max(tims), 'sec')
print('avg', sum(lens) / cnt, 'moves', 'max', max(lens), 'moves')
print('longest time scramble', scrambles[tims.index(max(tims))])