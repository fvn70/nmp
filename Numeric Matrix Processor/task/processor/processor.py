from array import array
from math import floor

import numpy as np

MENU = """
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
"""

MENU_T = """
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
"""

def read_matrix(num):
    txt = 'first' if num == 1 else 'second' if num == 2 else ''
    msg = f"Enter size of {txt} matrix: "
    n, m = map(int, input(msg).split(' '))
    print(f'Enter {txt} matrix:')
    # arr = np.empty((n, m), dtype=float)
    lst = []
    for i in range(n):
        lst.append(input().split(' '))
        # arr[i] = [float(v) for v in s.split(' ')]
    if '.' in str(lst):
        arr = np.array(lst, dtype=float)
    else:
        arr = np.array(lst, dtype=int)
    return arr

def print_matrix(arr):
    for i in range(len(arr)):
        s = ' '.join([str(v) for v in arr[i]])
        print(s)

def add_matrix(arr1, arr2):
    if arr1.shape == arr2.shape:
        print('The result is:')
        print_matrix(arr1 + arr2)
    else:
        print('The operation cannot be performed')

def mul_matrix(arr1, arr2):
    if arr1.shape[1] == arr2.shape[0]:
        print('The result is:')
        print_matrix(arr1 @ arr2)
    else:
        print('The operation cannot be performed')

def k_matrix(arr, k):
    return k * arr

def do_add():
    arr1 = read_matrix(1)
    arr2 = read_matrix(2)
    add_matrix(arr1, arr2)

def do_mul_2():
    arr1 = read_matrix(1)
    arr2 = read_matrix(2)
    mul_matrix(arr1, arr2)

def do_mul_k():
    arr = read_matrix(0)
    k = input('Enter constant: ')
    if '.' in k:
        k = float(k)
    else:
        k = int(k)
    print('The result is:')
    print_matrix(k_matrix(arr, k))

def trans_matrix(arr, cmd):
    n = arr.shape[0]
    arr_new = arr.copy()
    for i in range(n):
        for j in range(n):
            if cmd == 1:
                arr_new[i, j] = arr[j, i]
            elif cmd == 2:
                arr_new[i, j] = arr[n-j-1, n-i-1]
            elif cmd == 3:
                arr_new[i, j] = arr[i, n-j-1]
            elif cmd == 4:
                arr_new[i, j] = arr[n-i-1, j]
    return arr_new

def do_trans():
    print(MENU_T)
    cmd = int(input('Your choice: '))
    arr = read_matrix(0)
    print_matrix(trans_matrix(arr, cmd))

def get_minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def det_matrix(m):
    #base case for 2x2 matrix
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    det = 0
    for c in range(len(m)):
        det += ((-1)**c) * m[0][c] * det_matrix(get_minor(m, 0, c))
    return det

def inv_matrix(m):
    det = det_matrix(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/det, -1*m[0][1]/det],
                [-1*m[1][0]/det, m[0][0]/det]]
    #find matrix of cofactors
    cof = []
    for r in range(len(m)):
        cof_row = []
        for c in range(len(m)):
            mr = get_minor(m, r, c)
            cof_row.append(((-1)**(r+c)) * det_matrix(mr))
        cof.append(cof_row)
    cof = trans_matrix(np.array(cof), 1).tolist()
    for r in range(len(cof)):
        for c in range(len(cof)):
            cof[r][c] = cof[r][c]/det
    return cof

def do_det():
    arr = read_matrix(0).tolist()
    print('The result is:\n', det_matrix(arr))

def do_inv():
    arr = read_matrix(0).tolist()
    print('The result is:')
    print_matrix(inv_matrix(arr))

def menu():
    while True:
        print(MENU)
        cmd = int(input('Your choice: '))
        if cmd == 0:
            break
        elif cmd == 1:
            do_add()
        elif cmd == 2:
            do_mul_k()
        elif cmd == 3:
            do_mul_2()
        elif cmd == 4:
            do_trans()
        elif cmd == 5:
            do_det()
        elif cmd == 6:
            do_inv()
        else:
            print('Wrong choice!')
    return


menu()
