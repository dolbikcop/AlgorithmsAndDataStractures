from typing import List, Tuple


def main():
    n = int(input())
    bakters = []
    for i in range(n):
        input_string = input().split()
        bakters.append((int(input_string[0]), int(input_string[1])))
    plants_temp = list(map(int, input().split()))
    #bakters = sorted(bakters, key=lambda x: x[0])
    perebor(bakters, plants_temp)


def perebor(arr: List[Tuple[int, int]], dic: List[int]):
    for i in dic:
        c = 0
        for j in arr:
            if j[0] <= i <= j[1]:
                c += 1
        print(c)


main()
