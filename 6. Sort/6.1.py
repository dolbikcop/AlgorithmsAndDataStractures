import sys


def main():
    input_string = list(map(int, sys.stdin.readline().split()))
    length = len(input_string)
    iter = int(sys.stdin.readline())
    current_iter = 0
    is_output = True
    is_sorted = length - 1
    while is_sorted > 0:
        is_sorted = 0
        if is_output and current_iter == iter:
            print(*input_string)
            is_output = False
        for i in range(length-1):
            if input_string[i] > input_string[i+1]:
                input_string[i], input_string[i+1] = input_string[i+1], input_string[i]
                is_sorted = i
        current_iter += 1
        length = is_sorted + 1
    if is_output:
        print(*input_string)
    print(*input_string)

main()