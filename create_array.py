# coding:utf-8
from collections import deque
import csv

from basic_functions import *

def create_cross_trans():
    cross_trans = [[-1 for _ in range(8 * 11)] for _ in range(12 ** 5)]
    for idx in range(12 ** 5):
        if idx % 1000 == 0:
            print(idx)
        state = idx2state(idx, 0, 0)
        for pins_idx in range(8):
            for twist in range(1, 12):
                n_idx = pins_idx * 11 + twist - 1
                res = state2idx(move(state, pins_num_candidate[0][pins_idx], twist))[0]
                cross_trans[idx][n_idx] = res
    with open('cross_trans.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for line in cross_trans:
            writer.writerow(line)

def create_corner_trans():
    corner_trans = [[-1 for _ in range(14 * 11)] for _ in range(12 ** 4)]
    for idx in range(12 ** 4):
        if idx % 1000 == 0:
            print(idx)
        state = idx2state(0, 0, idx * 144)
        for pins_idx in range(14):
            for twist in range(1, 12):
                n_idx = pins_idx * 11 + twist - 1
                res = state2idx(move(state, pins_num_candidate[2][pins_idx], twist))[2] // 144
                corner_trans[idx][n_idx] = res
    with open('corner_trans.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for line in corner_trans:
            writer.writerow(line)

def create_cross_cost():
    cross_cost = [1000 for _ in range(12 ** 5)]
    solved = [[i for _ in range(14)] for i in range(12)]
    for i in range(12):
        cross_cost[state2idx(solved[i])[1]] = 0
    que = deque([[state2idx(solved[i])[0], 0] for i in range(12)])
    cnt = 0
    phase = 0
    while que:
        cnt += 1
        if cnt % 1000 == 0:
            print(cnt, len(que))
        state_idx, cost = que.popleft()
        n_cost = cost + 1
        for pin_idx in range(8):
            for twist in range(1, 12):
                n_idx = cross_trans[state_idx][pin_idx * 11 + twist - 1]
                if cross_cost[n_idx] > n_cost:
                    cross_cost[n_idx] = n_cost
                    que.append([n_idx, n_cost])
    with open('cross_cost.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(cross_cost)

def create_corner_cost():
    corner_cost = [1000 for _ in range(12 ** 6)]
    solved = [0 for _ in range(14)]
    corner_cost[state2idx(solved)[2]] = 0
    que = deque([[state2idx(solved)[2], 0]])
    cnt = 0
    phase = 2
    while que:
        cnt += 1
        if cnt % 1000 == 0:
            print(cnt, len(que))
        state_idx, cost = que.popleft()
        lower_idx = state_idx % 12
        state_idx //= 12
        upper_idx = state_idx % 12
        state_idx //= 12
        n_cost = cost + 1
        for pin_idx, pin_num in enumerate(pins_num_candidate[phase]):
            for twist in range(1, 12):
                n_upper_idx = upper_idx
                n_lower_idx = lower_idx
                if pins_candidate[pin_num][1]:
                    n_upper_idx += twist
                    n_upper_idx %= 12
                else:
                    n_lower_idx -= twist
                    n_lower_idx %= 12
                n_idx = corner_trans[state_idx][pin_idx * 11 + twist - 1] * 144 + n_upper_idx * 12 + n_lower_idx
                if corner_cost[n_idx] > n_cost:
                    corner_cost[n_idx] = n_cost
                    que.append([n_idx, n_cost])
    with open('corner_cost.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(corner_cost)

#create_cross_trans()

create_corner_trans()

cross_trans = []
with open('cross_trans.csv', mode='r') as f:
    for line in map(str.strip, f):
        cross_trans.append([int(i) for i in line.replace('\n', '').split(',')])
create_cross_cost()

corner_trans = []
with open('corner_trans.csv', mode='r') as f:
    for line in map(str.strip, f):
        corner_trans.append([int(i) for i in line.replace('\n', '').split(',')])
create_corner_cost()
