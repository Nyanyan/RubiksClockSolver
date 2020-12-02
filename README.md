# RubiksClockSolver
Rubik's Clock Solver written in Python

## Usage

### Set up

```
$ python create_array.py
```

Please wait few minutes. Four CSV files are created.

### How to Use in Code

Sample code:

```python
from solver import solver
# Please wait few seconds before initialized
scrambled_cube = [11, 8, 6, 3, 3, 10, 4, 9, 8, 9, 3, 10, 3, 9]
# WCA scramble for this cube: UR6+ DR5- DL5- UL3+ U4+ R6+ D1- L3- ALL5+ y2 U6+ R0+ D5- L5+ ALL3- DR
solution = solver(scrambled_cube)
print(solution)
# ['Uddd U -3', 'dUdd d 6', 'dddU U 2', 'UddU d 2', 'ddUU U 3', 'UUUd d 1', 'UdUU d 6', 'UdUU U 4', 'dUUU d -5']
print(' / '.join(solution))
# Uddd U -3 / dUdd d 6 / dddU U 2 / UddU d 2 / ddUU U 3 / UUUd d 1 / UdUU d 6 / UdUU U 4 / dUUU d -5
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

## Is this solver optimal?

Please see this graph. This is made by ```test_statics.py``` and the number of solves is 1000.

![graph](https://github.com/Nyanyan/RubiksClockSolver/blob/main/graph.png)

The average rotation of this solver is 9.55, while 9.43 if optimal.

I think this solver rarely returns detour solutions.

## How fast is this solver?

0.078 second for average, 1.0 second maximum when I solved 1000 scrambles.

