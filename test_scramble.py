from time import time
from solver import solver

scramble = [11, 7, 6, 9, 6, 2, 1, 3, 2, 1, 2, 4, 7, 6]#[int(i) for i in input('input the scramble: ').split()]
strt = time()
solution = solver(scramble)
print('scramble:')
print(scramble)
print(len(solution), 'moves')
print('solution:')
print(' / '.join(solution))
print(time() - strt, 'sec')
