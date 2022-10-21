import numpy as np

def read_matrix():
    n, m = map(int, input().split(' '))
    arr = np.empty((n, m), dtype=int)
    for i in range(n):
        s = input()
        arr[i] = [int(v) for v in s.split(' ')]
    return arr

def print_matrix(arr):
    for i in range(arr.shape[0]):
        s = ' '.join([str(v) for v in arr[i]])
        print(s)

def add_matrix(arr1, arr2):
    if arr1.shape == arr2.shape:
        print_matrix(arr1 + arr2)
    else:
        print('ERROR')

def mul_matrix(arr, k):
    return k * arr

def stage1():
    arr1 = read_matrix()
    arr2 = read_matrix()
    arr = arr1 + arr2
    print_matrix(arr)

def stage2():
    arr = read_matrix()
    k = int(input())
    print_matrix(mul_matrix(arr, k))

stage2()
