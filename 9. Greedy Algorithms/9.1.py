def main():
    n, w = map(int, input().split())
    arr = []
    for i in range(n):
        p, s = map(int, input().split())
        arr.append((p, s))
    arr.sort(key=lambda x: x[0]/x[1], reverse=True)

    money = 0
    for i in arr:
        if w <= i[1]:
            money += w * i[0] / i[1]
            break
        w -= i[1]
        money += i[0]

    print("{0:.2f}".format(money))

main()