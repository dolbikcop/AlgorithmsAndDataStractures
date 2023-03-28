def main():
    s = input()
    length = len(s)
    c=0
    for i in s:
        c+=1
        if length%c!=0:
            continue
        sub = s[:c]
        m = s.count(sub)
        if m == length / c:
            k = m
            break
    print(k, sub)

main()