import sys
from collections import deque
def main():
    deq = deque()
    while True:
        command = sys.stdin.readline().split()
        if len(command) == 3:
            deq.append((int(command[2]), command[1]))
            index = len(deq) - 2
            while index > -1:
                if deq[index][0] >= deq[index+1][0]:
                    break
                deq[index], deq[index+1] = deq[index+1], deq[index]
                index-=1
            print('ok')
        elif len(command) == 2:
            if len(deq) == 0:
                print(-1)
            elif command[1] == 'top':
                print(deq.popleft()[1])
            elif command[0] == 'pop':
                for i in range(len(deq)-1, 0, -1):
                    if deq[i][0] == int(command[1]) and deq[i-1][0] != int(command[1]):
                        deq[i], deq[i-1] = deq[i-1], deq[i]
                print(deq.popleft()[1] if deq[0][0] == int(command[1]) else -1)
            else:
                count = 0
                while True:
                    for i in range(len(deq) - 1, 0, -1):
                        if deq[i][0] == int(command[1]) and deq[i - 1][0] != int(command[1]):
                            deq[i], deq[i - 1] = deq[i - 1], deq[i]
                    if len(deq)!=0 and deq[0][0] == int(command[1]):
                        print(deq.popleft()[1], end=' ')
                        count += 1
                    else:
                        break
                print(-1 if count == 0 else '')
        elif command[0] == 'size':
            print(len(deq))
        elif command[0] == 'clear':
            deq.clear()
            print('ok')
        else:
            print('bye')
            return
main()