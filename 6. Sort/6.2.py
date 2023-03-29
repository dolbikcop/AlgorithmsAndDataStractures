def main():
    string = list(map(int, input().split()))
    l = len(string)
    middle = [*sorted(string[0:l // 2 + l % 2]), *string[l // 2 + l % 2:]]
    print(*middle)
    print(*sorted(string))

main()