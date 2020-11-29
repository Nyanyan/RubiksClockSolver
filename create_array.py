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
            for amount in range(1, 12):
                n_idx = pins_idx * 11 + amount - 1
                res = state2idx(move(state, pins_num_candidate[0][pins_idx], amount))[0]
                cross_trans[idx][n_idx] = res
    with open('cross_trans.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for line in cross_trans:
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
    que = deque([[solved, 0]])
    cnt = 0
    phase = 2
    while que:
        cnt += 1
        if cnt % 1000 == 0:
            print(cnt, len(que))
        state, cost = que.popleft()
        n_cost = cost + 1
        for pin_num in pins_num_candidate[phase]:
            for twist in range(1, 12):
                n_state = move(state, pin_num, twist)
                n_idx = state2idx(n_state)[phase]
                if corner_cost[n_idx] > n_cost:
                    corner_cost[n_idx] = n_cost
                    que.append([n_state, n_cost])
    with open('corner_cost.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(corner_cost)

create_cross_trans()
cross_trans = []
with open('cross_trans.csv', mode='r') as f:
    for line in map(str.strip, f):
        cross_trans.append([int(i) for i in line.replace('\n', '').split(',')])
create_cross_cost()
create_corner_cost()
