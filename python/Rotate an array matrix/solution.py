'''
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

Clockwise rotation:

[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]

Counter-clockwise rotation:

[
  [3, 6, 9],
  [2, 5, 8],
  [1, 4, 7]
]

- - - - - - - - - - 

POS   |   0  1  2  3  4  5  6  7  8
------------------------------------
ORIGN = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

__CLK = [ 7, 4, 1, 8, 5, 2, 9, 6, 3 ]
    P = ( P + 2 ) % 9

 Y = número de linhas
 y = coordenada vertical   (top -> down,   inicio em 1)
 x = coordenada horizontal (left -> right, inicio em 0)

    Posição = (Y - y) + Y * x
    1 = (3 - 1) + 3 * 0 = 2
    2 = (3 - 1) + 3 * 1 = 5
    3 = (3 - 1) + 3 * 2 = 8
    4 = (3 - 2) + 3 * 0 = 1
    5 = (3 - 2) + 3 * 1 = 4
    6 = (3 - 2) + 3 * 2 = 7
    7 = (3 - 3) + 3 * 0 = 0
    8 = (3 - 3) + 3 * 1 = 3
    9 = (3 - 3) + 3 * 2 = 6

    1: 0, 2
    2: 1, 5
    3: 2, 8
    4: 3, 1
    5: 4, 4
    6: 5, 7
    7: 6, 0
    8: 7, 3
    9: 8, 6


C_CLK = [ 3, 6, 9, 2, 5, 8, 1, 4, 7 ]
	P = REVERSE((P + 2) % 9)

 -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  

        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12]]

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ( P + 3 ) % 9

[10, 7, 4, 1, 11, 8, 5, 2, 12, 9, 6, 3]                 

'''

'''
[[01,02,03],
 [04,05,06],
 [07,08,09],
 [10,11,12]]

[[10,07,04,01],
 [11,08,05,02],
 [12,09,06,03]]

P 00 01 02 03 04 05 06 07 08 09 10 11
 [01,02,03,04,05,06,07,08,09,10,11,12]
 [10,07,04,01,11,08,05,02,12,09,06,03]

 01 = (4 - 1) + 4 * 0 = 03
 04 = (4 - 2) + 4 * 0 = 02
 07 = (4 - 3) + 4 * 0 = 01
 10 = (4 - 4) + 4 * 0 = 00

 02 = (4 - 1) + 4 * 1 = 07
 03 = (4 - 1) + 4 * 2 = 11

 05 = (4 - 2) + 4 * 1 = 06
 06 = (4 - 2) + 4 * 2 = 10

 08 = (4 - 3) + 4 * 1 = 05
 09 = (4 - 3) + 4 * 2 = 09

 11 = (4 - 4) + 4 * 1 = 04
 12 = (4 - 4) + 4 * 2 = 08

 Y = número de linhas
 y = coordenada vertical   (top -> down,   inicio em 1)
 x = coordenada horizontal (left -> right, inicio em 0)
 Posição = (Y - y) + Y * x


 01: 00, 03
 02: 01, 07
 03: 02, 11
 04: 03, 02
 05: 04, 06
 06: 05, 10
 07: 06, 01
 08: 07, 05
 09: 08, 09
 10: 09, 00
 11: 10, 04
 12: 11, 08

 Y = número de linhas
 y = coordenada vertical   (top -> down,   inicio em 1)
 x = coordenada horizontal (left -> right, inicio em 0)
 Posição = (Y - y) + Y * x

'''

def rotate(matrix, direction): 
    rows, cols = len(matrix), len(matrix[0])

    vec = [ None for _ in range(rows * cols) ]
    squashed_pos = lambda Y, y, x : (Y - y - 1 ) + Y * x

    for y, row in enumerate(matrix):
        for x, el in enumerate(row):
            pos = squashed_pos(rows, y, x)
            vec[pos] = el

    if direction == "counter-clockwise":
        vec.reverse()

    print("rows", rows, "cols", cols)

    print("direction", direction)
    print(vec)

    res = [ vec[n*rows : rows * (n + 1)] for n in range(cols) ]

    print(res)
    return res
