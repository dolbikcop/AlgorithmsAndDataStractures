import random
from typing import List


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_index_element(arr, k))


def partition(arr: List[int], l: int, r: int) -> int:
    if r - l < 1:
        return l
    i = l
    X = arr[r - 1 if r > 0 else 0]
    j = r - 2 if r > 1 else 0

    while i <= j:
        while arr[i] < X:
            i += 1
        while arr[j] >= X and j > 0:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            break
    arr[i], arr[r-1 if r > 0 else 0] = arr[r-1 if r > 0 else 0], arr[i]
    return i


def get_index_element(arr: List[int], index: int) -> int:
    l = 0
    r = len(arr)
    while l + 1 < r:
        m = partition(arr, l, r)
        if m == index:
            return arr[m]
        elif m < index:
            l = m + 1
        else:
            r = m
    return arr[l]


main()
