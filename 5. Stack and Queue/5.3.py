from collections import deque


def main():
    queue_first = deque()
    queue_second = deque()

    n = int(input())

    for i in range(n):
        data = input().split()
        if len(data) == 2:
            command = data[0]
            knigth = data[1]
            if command == '!':
                queue_first.appendleft(knigth)
            elif command == '+':
                queue_second.append(knigth)
            elif command == '*':
                queue_second.appendleft(knigth)
            if len(queue_first) - 1 > len(queue_second):
                queue_second.appendleft(queue_first.pop())
            elif len(queue_first) < len(queue_second):
                queue_first.append(queue_second.popleft())
        else:
            print(queue_first.popleft())
            if len(queue_first) < len(queue_second):
                queue_first.append(queue_second.popleft())

main()