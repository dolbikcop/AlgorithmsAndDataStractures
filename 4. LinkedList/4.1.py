from collections import deque


def main():
    input = open('input.txt', 'r')
    output = open('output.txt', 'w')
    stack = deque(maxlen=int(input.readline()))
    while True:
        string = input.readline().split()
        if len(string) == 2:
            stack.append(string[1])
            output.write('ok')
        elif string[0] == 'pop':
            output.write(stack.pop())
        elif string[0] == 'count':
            output.write(str(len(stack)))
        else:
            output.write('bye')
            input.close()
            output.close()
            return
        output.write('\n')
main()
