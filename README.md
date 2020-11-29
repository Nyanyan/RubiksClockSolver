# RubiksClockSolver
Rubik's Clock Solver written in Python

## Usage

### Set up

```
$ python create_array.py
```

Please wait few minutes.

### How to Use in Code

Sample code:

```python
from solver import solver
scrambled_cube = [11, 8, 6, 3, 3, 10, 4, 9, 8, 9, 3, 10, 3, 9]
# WCA scramble for this cube: UR6+ DR5- DL5- UL3+ U4+ R6+ D1- L3- ALL5+ y2 U6+ R0+ D5- L5+ ALL3- DR
solution = solver(scrambled_cube)
print(res)
# ['dddd d -4', 'Uddd U 6', 'UdUd U 1', 'ddUU U 5', 'UUUd d 6', 'UUdU d -5', 'UUdU U -2', 'UdUU d 1', 'dUUU U -1']
print(' / '.join(solution))
# dddd d -4 / Uddd U 6 / UdUd U 1 / ddUU U 5 / UUUd d 6 / UUdU d -5 / UUdU U -2 / UdUU d 1 / dUUU U -1
```

```scrambled_cube``` is the scramble. Each index is related to each clock. Details:

```
clock numbering:
upper
 5  0  6
 1  2  3
 7  4  8

lower
 6  9  5
10 11 12
 8 13  7

solved state: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

```solution``` is the solution of the scramble. The notation is:

The first string means the state of pins, which is numbered as below.

```
pin numbering:
upper face
0 1
2 3
```

```U``` means the pin is pulled, ```d``` means pushed.

The second character means which face to rotate. ```U``` means upper face, ```d``` means the lower face.

The following number is how many times to rotate. ```+3``` means 90 degrees clockwise, ```-1``` means 30 degrees counterclockwise.

For example, ```Uddd U 6``` means ```UL 6+```, and ```dUUU d 3``` means ```y2 UR 3-``` shortly in WCA scramble.

