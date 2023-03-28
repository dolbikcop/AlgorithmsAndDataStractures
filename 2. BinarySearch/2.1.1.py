import sys
def main():
    heights_orks = [int(i) for i in sys.stdin.readline().split()]
    heights_grimma = [int(i) for i in sys.stdin.readline().split()]

    count = len(heights_orks)
    dic = {}
    for i in range(count):
        if heights_orks[i] not in dic:
            dic[heights_orks[i]] = [i]
        else:
            dic[heights_orks[i]].append(i)

    for i in heights_grimma:
        if i not in dic.keys():
            print(0, end=' ')
        else:
            max_val = 0
            count_i = len(dic[i])
            for j, h in enumerate(dic[i]):
                max_val = max((j+1) * (count - (h + count_i - j)),  max_val)
            print(max_val, end=' ')
main()
#1 1 2 2 2 2 1 1 1
#1 2 1
