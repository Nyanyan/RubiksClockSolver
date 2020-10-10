from time import time
from solver import solver

scramble = [int(i) for i in input('input the scramble: ').split()]
strt = time()
solution = solver(scramble)
print(len(solution), 'moves')
print('solution:')
print(' / '.join(solution))
print(time() - strt, 'sec')
