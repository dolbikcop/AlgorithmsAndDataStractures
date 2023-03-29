def main():
    string = list(map(int, input().split()))
    l = len(string)
    if l < 2:
        print(*string)
    for i in range(l-1):
        min_val = string[i]
        min_ind = i
        for j in range(i+1, l):
            if string[j] < min_val:
                min_val = string[j]
                min_ind = j
        string[i], string[min_ind] = string[min_ind], string[i]
        if i+1 == l // 2:
            print(*string)
    print(*string)
main()
