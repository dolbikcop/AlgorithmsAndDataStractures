from collections import namedtuple, deque
from typing import List
Gymnast = namedtuple("Gymnast", "name mass weight")


def solve(boxes: List[Gymnast]):
    boxes.sort(key=lambda x: (x.weight + x.mass))
    q = []
    result = deque()
    sum_w = 0
    cnt = 0
    for i in range(0, len(boxes)):
        if boxes[i].mass >= sum_w:
            cnt += 1
            sum_w += boxes[i].weight
            q.append(boxes[i])
            result.append(boxes[i].name)
            q.sort(key=lambda x: x.weight)
        elif len(q) > 0 and q[-1].weight > boxes[i].weight:
            sum_w -= q.pop().weight
            result.pop()
            result.append(boxes[i].name)
            q.append(boxes[i])
            q.sort(key=lambda x: x.weight)
            sum_w += boxes[i].weight
    return cnt, result


def main():
    n = int(input())
    arr = []
    for i in range(n):
        name, mass, weight = input().split(';')
        arr.append(Gymnast(name, int(mass), int(weight)))
    cnt, gmnsts = solve(arr)
    print(cnt)
    for i in gmnsts:
        print(i)

main()
