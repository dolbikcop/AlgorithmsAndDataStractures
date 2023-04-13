from typing import List

global_counter = 0
def get_marks(arr: List[int], ind: int, max_val: int, min_val: int):
    if len(arr) > ind:
        for i in range(min_val+(len(arr)-ind)-1, max_val+1):
            if ind == 0 or arr[ind-1] > i:
                arr[ind] = i
                get_marks(arr, ind+1, i+1, min_val)
    else:
        print(*arr)
        global global_counter
        global_counter += 1
def main():
    n, min_val, max_val = map(int, input().split())
    get_marks([0]*n, 0, max_val, min_val)
    print(global_counter)
main()