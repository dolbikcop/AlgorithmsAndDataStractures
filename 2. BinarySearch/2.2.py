import sys


def main():
    n, m, l = map(int, sys.stdin.readline().split())
    legs = []
    hands = []
    for i in range(n):
        legs.append(list(map(int, sys.stdin.readline().split())))
    for i in range(m):
        hands.append(list(map(int, sys.stdin.readline().split())))
    q = int(sys.stdin.readline())
    for i in range(q):
        f, s = map(int, sys.stdin.readline().split())
        left = 0
        right = l - 1
        while left <= right:
            middle = (left + right) // 2
            if hands[s][middle] > legs[f][middle]:
                left = middle + 1
            elif hands[s][middle] < legs[f][middle]:
                right = middle - 1
            else:
                break
        print((left + right) // 2)

main()