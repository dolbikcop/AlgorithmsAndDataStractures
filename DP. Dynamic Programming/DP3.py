def main():
    substrings = []
    string = input()
    length = len(string)
    k = 1
    for i in range(0, length):
        substrings.append([0] * (length - i))
        for j in range(0, length - i):
            sub = string[j:(j + i + 1)]
            if i + 1 > 4:
                sub, k = collapse(sub, i + 1)
                sub = collapse_by_substrings(sub, substrings, len(sub), j)
            substrings[i][j] = sub if k == 1 else f'{k}({sub})'
    print(*substrings[-1])


# aaaaaxaxax
# абабабавававабабабававав
def collapse_by_substrings(string: str, substrings, length: int, index: int):
    result = string
    if length > 4:
        for end in range(0, length-1):
            left = substrings[end][index]
            right = substrings[length - end - 2][index + end + 1]
            if len(left) + len(right) < len(result):
                result = left + right
    return result


def collapse(string: str, length: int):
    res_sub = string
    k = 1
    for i in range(1, length // 2 + 1):
        if length % i != 0:
            continue
        sub = string[:i]
        if string == sub * (length // i) and i + 3 < length:
            res_sub = sub
            k = length // i
            break
    return res_sub, k


main()
