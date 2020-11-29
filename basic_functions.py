# coding:utf-8

def move_clocks_p(pins, direction):
    res = []
    if direction: # move upper clocks
        clock_candidate = [[5, 0, 1, 2], [0, 6, 2, 3], [1, 2, 7, 4], [2, 3, 4, 8]]
        for i, j in enumerate(pins):
            if j:
                res.extend(clock_candidate[i])
    else: # move lower clocks
        clock_candidate = [[5, 9, 12, 11], [9, 6, 11, 10], [12, 11, 7, 13], [11, 10, 13, 8]]
        for i, j in enumerate(pins):
            if not j:
                res.extend(clock_candidate[i])
    return set(res)

def move(state, num, twist):
    pins, direction = pins_candidate[num]
    move_clocks = move_clocks_p(pins, direction)
    res = [i for i in state]
    for i in move_clocks:
        if direction or i in {5, 6, 7, 8}:
            res[i] += twist
        else:
            res[i] -= twist
        res[i] %= 12
    return res

def state2idx(state):
    state_upper = [state[i] for i in (0, 1, 2, 3, 4)]
    state_lower = [state[i] for i in (9, 10, 11, 12, 13)]
    state_corner = [state[i] for i in (5, 6, 7, 8)]
    res_upper = 0
    for i in range(5):
        res_upper *= 12
        res_upper += state_upper[i]
    res_lower = 0
    for i in range(5):
        res_lower *= 12
        res_lower += state_lower[i]
    res_corner = 0
    for i in range(4):
        res_corner *= 12
        res_corner += state_corner[i]
    res_corner *= 12
    res_corner += state[0]
    res_corner *= 12
    res_corner += state[9]
    return res_lower, res_upper, res_corner

def idx2state(idx_lower, idx_upper, idx_corner):
    res = [-1 for _ in range(14)]
    for i in (4, 3, 2, 1, 0):
        res[i] = idx_upper % 12
        idx_upper //= 12
    for i in (13, 12, 11, 10, 9):
        res[i] = idx_lower % 12
        idx_lower //= 12
    idx_corner //= 144
    for i in (8, 7, 6, 5):
        res[i] = idx_corner % 12
        idx_corner //= 12
    return res

pins_candidate = [
    [[False, False, False, False], 0], 
    [[True, False, False, False], 0], [[True, False, False, False], 1], [[False, True, False, False], 0], [[False, True, False, False], 1], [[False, False, True, False], 0], [[False, False, True, False], 1], [[False, False, False, True], 0], [[False, False, False, True], 1], 
    [[True, True, False, False], 0], [[True, True, False, False], 1], [[True, False, True, False], 0], [[True, False, True, False], 1], [[True, False, False, True], 0], [[True, False, False, True], 1], [[False, True, True, False], 0], [[False, True, True, False], 1], [[False, True, False, True], 0], [[False, True, False, True], 1], [[False, False, True, True], 0], [[False, False, True, True], 1], 
    [[True, True, True, False], 0], [[True, True, True, False], 1], [[True, True, False, True], 0], [[True, True, False, True], 1], [[True, False, True, True], 0], [[True, False, True, True], 1], [[False, True, True, True], 0], [[False, True, True, True], 1], 
    [[True, True, True, True], 1]
    ]

pins_num_candidate = [[9, 11, 17, 19, 21, 23, 25, 27], [20, 12, 18, 10, 6, 8, 2, 4], [0, 1, 3, 5, 7, 13, 14, 15, 16, 22, 24, 26, 28, 29]]

set_pins_num_candidate = [set(i) for i in pins_num_candidate]

print('basic functions initialized')
