from array import array

import numpy as np

MENU = """
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
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
    for i in range(arr.shape[0]):
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
        else:
            print('Wrong choice!')
    return


menu()
