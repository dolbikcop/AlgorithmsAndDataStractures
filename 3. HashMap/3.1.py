def main():
    first = input().split()
    second = list(input().split())
    d = {}
    for i in first:
        if i not in d.keys():
            d[i] = second.count(i)
        print(d[i], end=' ')

if __name__ == '__main__':
    main()