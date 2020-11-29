# coding:utf-8
'''TO TEST THIS CODE, PLEASE EXECUTE TEST_SCRAMBLE.PY OR TEST_STATISTICS.PY'''
'''
clock numbering

upper
 5  0  6
 1  2  3
 7  4  8

lower
 6  9  5
10 11 12
 8 13  7

solved: state == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

pin numbering

upper
0 1
2 3
'''

from basic_functions import *
from copy import deepcopy

# Return distances from solved state
def distance_phase01(state_idx):
    return cross_cost[state_idx]

# Return distances from solved state
def distance_phase2(state_idx):
    return corner_cost[state_idx]

def move_idx(phase, state_idx, pin_num, twist):
    idx = pins_num_candidate[phase].index(pin_num)
    if phase < 2:
        return cross_trans[state_idx][idx * 11 + twist - 1]
    else:
        return corner_trans[state_idx][idx * 11 + twist - 1]

# Search the phase solution in phase0 & 1
def search_phase01(phase, depth, state_idx, strt_idx):
    global phase_solution
    solved_solution = []
    dis = distance_phase01(state_idx)
    n_depth = depth - 1
    for idx, pin_num in enumerate(pins_num_candidate[phase][strt_idx:]):
        n_strt_idx = strt_idx + idx + 1
        for twist in range(1, 12):
            twist_proc = twist if phase == 0 else (-twist) % 12
            n_state_idx = move_idx(phase, state_idx, pin_num, twist_proc)
            n_dis = distance_phase01(n_state_idx)
            if n_dis >= dis or n_dis > depth:
                continue
            phase_solution.append([pin_num, twist])
            if n_dis == 0:
                solved_solution.append([[i for i in j] for j in phase_solution])
            elif n_dis <= n_depth:
                tmp = search_phase01(phase, n_depth, n_state_idx, n_strt_idx)
                if tmp:
                    solved_solution.extend(tmp)
            phase_solution.pop()
    return solved_solution

# Search the phase solution in phase2
def search_phase2(depth, state_idx, strt_idx):
    global phase_solution
    phase = 2
    solved_solution = []
    dis = distance_phase2(state_idx)
    n_depth = depth - 1
    lower_idx = state_idx % 12
    state_idx //= 12
    upper_idx = state_idx % 12
    state_idx //= 12
    for pin_idx, pin_num in enumerate(pins_num_candidate[phase]):
        n_strt_idx = strt_idx + pin_idx + 1
        for twist in range(1, 12):
            twist_proc = twist if phase == 0 else (-twist) % 12
            n_upper_idx = upper_idx
            n_lower_idx = lower_idx
            if pins_candidate[pin_num][1]:
                n_upper_idx += twist
                n_upper_idx %= 12
            else:
                n_lower_idx -= twist
                n_lower_idx %= 12
            n_state_idx = move_idx(phase, state_idx, pin_num, twist_proc) * 144 + n_upper_idx * 12 + n_lower_idx
            n_dis = distance_phase2(n_state_idx)
            if n_dis >= dis or n_dis > depth:
                continue
            phase_solution.append([pin_num, twist])
            if n_dis == 0:
                return [[[i for i in j] for j in phase_solution]]
            elif n_dis <= n_depth:
                tmp = search_phase2(n_depth, n_state_idx, n_strt_idx)
                if tmp:
                    return tmp
            phase_solution.pop()
    return solved_solution

# The main part
def solver(problem_state):
    global phase_solution
    cost = 0
    solution = []
    states = [[0, state2idx(problem_state), []]]
    n_states = []
    for phase in range(2):
        min_ln = states[0][0]
        min_depth = 7
        for ln, state_idxes, pre_solution in states:
            if ln > min_ln:
                break
            state_idx = state_idxes[phase]
            solutions = []
            for depth in range(min_depth):
                phase_solution = []
                solutions = search_phase01(phase, depth, state_idx, 0)
                if solutions:
                    if depth + 1 < min_depth:
                        min_depth = depth + 1
                    break
            for solution in solutions:
                n_state = idx2state(state_idxes[0], state_idxes[1], state_idxes[2])
                for pin_num, twist in solution:
                    n_state = move(n_state, pin_num, twist)
                #print(n_state)
                n_solution = [[i for i in j] for j in pre_solution]
                n_solution.extend(solution)
                n_idxes = state2idx(n_state)
                if phase == 0:
                    plus_cost = max(cross_cost[n_idxes[1]], corner_cost[n_idxes[2]])
                else:
                    plus_cost = corner_cost[n_idxes[2]]
                n_states.append([len(n_solution) + plus_cost, n_idxes, n_solution])
        states = deepcopy(n_states)
        states.sort()
        n_states = []
        #print(phase, len(states), len(states[0][2]))

    phase = 2
    min_ln = states[0][0]
    min_depth = 7
    for ln, state_idxes, pre_solution in states:
        if ln > min_ln:
            break
        solutions = []
        for depth in range(min_depth):
            solutions = search_phase2(depth, state_idxes[2], 0)
            if solutions:
                if depth < min_depth:
                    min_depth = depth
                break
        for solution in solutions:
            n_solution = [[i for i in j] for j in pre_solution]
            n_solution.extend(solution)
            n_states.append([len(n_solution), n_solution])
    #print(phase, len(n_states), len(n_states[0][1]))
    
    n_states.sort()
    chosen_solution = n_states[0][1]
    chosen_solution.sort()
    chosen_solution_notation = [[pins_candidate[i[0]][0], pins_candidate[i[0]][1], i[1]] for i in chosen_solution]
    for i, arr in enumerate(chosen_solution_notation):
        pins, ud, twist = arr
        pins_str = ''.join(['U' if j else 'd' for j in pins])
        ud_str = 'U' if ud else 'd'
        if twist > 6:
            twist = twist - 12
        twist_str = str(twist)
        chosen_solution_notation[i] = pins_str + ' ' + ud_str + ' ' + twist_str
    return chosen_solution_notation

phase_solution = []

# Tables for prunning
with open('cross_cost.csv', mode='r') as f:
    cross_cost = [int(i) for i in f.readline().replace('\n', '').split(',')]
with open('corner_cost.csv', mode='r') as f:
    corner_cost = [int(i) for i in f.readline().replace('\n', '').split(',')]
cross_trans = []
with open('cross_trans.csv', mode='r') as f:
    for line in map(str.strip, f):
        cross_trans.append([int(i) for i in line.replace('\n', '').split(',')])
corner_trans = []
with open('corner_trans.csv', mode='r') as f:
    for line in map(str.strip, f):
        corner_trans.append([int(i) for i in line.replace('\n', '').split(',')])
print('solver initialized')


''' TEST
tmp = solver([6, 3, 10, 10, 6, 1, 5, 2, 7, 6, 3, 5, 7, 4]) #UR3- DR3- DL2+ UL3+ U1+ R4- D0+ L5+ ALL4+ y2 U4+ R5- D4+ L0+ ALL5- UR DL
#tmp = solver([10, 1, 7, 9, 3, 2, 2, 5, 8, 9, 6, 8, 1, 6]) # UR5+ DR3+ DL0+ UL5+ U4+ R6+ D4- L2+ ALL1- y2 U4+ R6+ D3- L2- ALL2+ DR
print(len(tmp), 'moves', ' / '.join(tmp))
'''