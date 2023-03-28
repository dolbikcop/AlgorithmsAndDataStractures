import sys

def different_elements(a: [], i: int) -> int:
    return len(a) - a.count(i)
def same_elements(a: [], i: int) -> int:
    return a.count(i)

def main():
    heights_orks = [int(i) for i in sys.stdin.readline().split()]
    heights_grimma = [int(i) for i in sys.stdin.readline().split()]

    dic = {}

    for h in heights_grimma:
        if h not in heights_orks:
            print(0, end='')
        elif h in dic.keys():
            print(dic[h], end='')
        else:
            left = 0
            right = len(heights_orks) - 1
            max_val = 0
            while left < right:
                i = (left + right) // 2
                dif = different_elements(heights_orks[i:], h)
                sam = same_elements(heights_orks[:i], h)
                if dif * sam > max_val:
                    max_val = dif * sam
                if same_elements(heights_orks[i:], h) < sam:
                    right = i
                else:
                    left = i + 1
            print(max_val, end=' ')
            dic[h] = max_val

main()