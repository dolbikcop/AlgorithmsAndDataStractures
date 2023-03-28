from collections import deque


def main():
    symbols = input().split()
    stack = deque()
    for i in symbols:
        if i.isdigit():
            stack.append(int(i))
        else:
            second = stack.pop()
            first = stack.pop()
            if i == '+':
                result = first + second
            elif i == '-':
                result = first - second
            elif i == '*':
                result = first * second
            elif i == '/':
                result = first // second
            elif i == '%':
                if second == 0:
                    result = 0
                else:
                    result = first % second
            stack.append(int(result))
    print(stack.pop())
main()