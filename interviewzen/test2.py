#!/usr/bin/env python3

def quicksort(A, i, k):
    if i < k:
        p = partition(A, i, k)
        quicksort(A, i, p - 1)
        quicksort(A, p + 1, k)

def partition(array, left, right):
    pivotIndex = (left+right)/2
    pivotValue = array[pivotIndex]
    array[pivotIndex], array[right] = array[right], array[pivotIndex]
    storeIndex = left
    for i in range(left, right):
        if array[i] < pivotValue:
            array[i], array[storeIndex] = array[storeIndex], array[i]
            storeIndex = storeIndex + 1
    array[storeIndex], array[right] = array[right], array[storeIndex]
    return storeIndex

if __name__ == '__main__':
    ll = [13, 9, 16, 5, 2, 0]
    quicksort(ll, 0, len(ll)-1)
    print(ll)
