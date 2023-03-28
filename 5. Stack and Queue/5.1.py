from collections import deque

def main():
    deq = deque()
    while True:
        command = input().split()
        if len(command) == 2:
            deq.append(command[1])
            print('ok')
        elif command[0] == 'size':
            print(len(deq))
        elif command[0] == 'pop':
            print(deq.popleft())
        elif command[0] == 'front':
            print(deq[0])
        elif command[0] == 'view':
            print(', '.join(deq))
        elif command[0] == 'clear':
            deq.clear()
            print('ok')
        else:
            print('bye')
            return
main()
