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
    print(i, len(res), 'moves', tim, 'sec')
    tims.append(tim)
    lens.append(len(res))
    scrambles.append(test_cube)
    cnt += 1
print(cnt, '/', num)
print('avg', sum(tims) / cnt, 'sec', 'max', max(tims), 'sec')
print('avg', sum(lens) / cnt, 'moves', 'max', max(lens), 'moves')
print('longest time scramble', scrambles[tims.index(max(tims))])

s = '''0                     1
1                   330
2                51,651
3             4,947,912
4           317,141,342
5        14,054,473,232
6       428,862,722,294
7     8,621,633,953,202
8   101,600,180,118,726
9   528,107,928,328,516
10   613,251,601,892,918
11    31,893,880,879,492
12                39,248'''
a = [[int(i) for i in j.split()] for j in s.replace(',', '').split('\n')]
sm = 0
al = 0
for i, j in a:
    sm += i * j
    al += j
sm /= al
print('if optimally solved, average may be', sm)
