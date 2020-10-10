# coding:utf-8
from collections import deque
import csv

from basic_functions import *

def create_cross_cost():
    cross_cost = [1000 for _ in range(12 ** 5)]
    solved = [[i for _ in range(14)] for i in range(12)]
    for i in range(12):
        cross_cost[state2idx(solved[i])[1]] = 0
    que = deque([[solved[i], 0] for i in range(12)])
    cnt = 0
    phase = 1
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
                if cross_cost[n_idx] > n_cost:
                    cross_cost[n_idx] = n_cost
                    que.append([n_state, n_cost])
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

create_cross_cost()
create_corner_cost()
