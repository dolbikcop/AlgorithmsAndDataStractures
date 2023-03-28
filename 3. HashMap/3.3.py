import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    plates = sys.stdin.readline().split()
    print(n, end=' ')
    for i in range(1, len(plates)):
        if i > len(plates) / 2:
            break
        flag = True
        for j in range(0, i+1):
            if plates[j+i-1] != plates[i-j]:
                flag = False
                break

        if flag: print(len(plates) - i, end=' ')


main()


def main():
    n, m = map(int, input().split())
    plates = input().split()
    print(n, end=' ')
    for i in range(1, n//2+1):
        flag = True
        for j in range(0, i+1):
            if plates[j+i-1] != plates[i-j]:
                flag = False
                break
        if flag: print(len(plates) - i, end=' ')
main()
