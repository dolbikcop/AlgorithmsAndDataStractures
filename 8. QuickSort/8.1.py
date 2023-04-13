from typing import List

def main():
    arr = list(map(int, input().split()))
    qsort(arr, 0, len(arr))
    print()
    print(arr)
def partition(arr: List[int], l, r:int) -> int:
    print(arr[r-1], end=' ')
    if r - l < 1:
        return l
    i = l
    j = r - 1
    X = arr[j]
    while i < j:
        while arr[i] < X:
            i += 1
        while arr[j] > X:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
        else:
            break
    return i
def qsort(arr: List[int], l: int, r: int):
    if r - l <= 1:
        return
    m = partition(arr, l, r)
    qsort(arr, l, m)
    qsort(arr, m, r)

main()