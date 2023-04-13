from typing import List


def merge(arr: List[int], l, m, r, buf: List[int]):
    global global_counter

    p1 = l
    p2 = m
    rp = 0

    while p1 < m or p2 < r:
        if p1 == m:
            buf[rp] = arr[p2]
            p2 += 1
        elif p2 == r:
            buf[rp] = arr[p1]
            p1 += 1
            global_counter += r - p2
        elif arr[p1] >= arr[p2]:
            buf[rp] = arr[p1]
            p1 += 1
            global_counter += r - p2
        else:
            buf[rp] = arr[p2]
            p2 += 1
        rp += 1
    for i in range(l, r):
        arr[i] = buf[i - l]
def mergeSort(arr, l, r, buf):
    if l + 1 < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m, buf)
        mergeSort(arr, m, r, buf)
        merge(arr, l, m, r, buf)

global_counter = 0
def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    mergeSort(arr, 0, n, [0]*n)
    print(global_counter)
main()