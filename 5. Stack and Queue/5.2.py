from collections import deque
from queue import PriorityQueue

class Priority:
    deq = deque
    def put(self, item: str, priority: int):
        pass
def main():
    deq = PriorityQueue()
    while True:
        command = input().split()
        if len(command) == 3:
            deq.put(int(command[2]), command[1])
            print('ok')
        elif len(command) == 2:
            if command[1] == 'top':
                print(-1 if deq.empty() else deq.get())
            elif command[0] == 'pop':
                print(deq.get(int(command[1])))
            else:
                a = deq.get(int(command[1]))
                print(a if not a == '' else -1)
        elif command[0] == 'size':
            print(deq.qsize())
        elif command[0] == 'clear':
            print('ok')
        else:
            print('bye')
            return
main()