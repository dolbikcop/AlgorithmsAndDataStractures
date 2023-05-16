from typing import List


def main():
    inp = input()
    arr = list(map(int, inp.split()))
    qsort(arr, 0, len(arr))
    print(*arr)


def partition(arr: List[int], l: int, r: int) -> int:
    if r - l < 1:
        return l
    i = l
    X = arr[r - 1 if r > 0 else 0]
    print(X)
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
    arr[i], arr[r - 1 if r > 0 else 0] = arr[r - 1 if r > 0 else 0], arr[i]
    return i


def qsort(arr: List[int], l: int, r: int):
    if r - l <= 1:
        return
    m = partition(arr, l, r)
    qsort(arr, l, m)
    qsort(arr, m + 1, r)


main()
