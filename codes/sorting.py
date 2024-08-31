import random

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1, n):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    print(array)

def bubbler_sort(array):
    n = len(array)
    flag = True
    while flag and n:
        n -= 1
        flag = False
        for i in range(n):
            if array[i+1] < array[i]:
                array[i+1], array[i] = array[i], array[i+1]
                flag = True
    print(array)
