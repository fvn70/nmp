import numpy as np

def read_matrix(n, m):
    arr = np.empty((n, m), dtype=int)
    for i in range(n):
        s = input()
        arr[i] = [int(v) for v in s.split(' ')]
    return arr

def print_matrix(arr):
    for i in range(arr.shape[0]):
        s = ' '.join([str(v) for v in arr[i]])
        print(s)

n1, m1 = map(int, input().split(' '))
arr1 = read_matrix(n1, m1)

n2, m2 = map(int, input().split(' '))
arr2 = read_matrix(n2, m2)

if n1 == n2 and m1 == m2:
    print_matrix(arr1 + arr2)
else:
    print('ERROR')
