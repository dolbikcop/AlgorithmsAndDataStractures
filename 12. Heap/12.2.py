import math
from typing import List, Sized


def main():
    heap = Heap()
    not_exit = True
    while not_exit:
        command = input().split()
        if len(command) == 2:
            element = int(command[1])
            heap.append(element)
            print('ok')
        elif command[0] == 'exit':
            not_exit = False
            print('bye')
        elif command[0] == 'min':
            print(heap.min())
        elif command[0] == 'size':
            print(len(heap))
        elif command[0] == 'structure':
            heap.print()
        elif command[0] == 'pop':
            print(heap.pop())


class Heap(Sized):
    def __init__(self):
        self.__heap: List[int] = []

    def __len__(self) -> int:
        return len(self.__heap)

    def append(self, other: int):
        self.__heap.append(other)
        self.sift_up(len(self) - 1)

    def pop(self):
        min_val = self.min()
        self.__heap[0], self.__heap[len(self) - 1] = self.__heap[len(self) - 1], self.__heap[0]
        del self.__heap[len(self) - 1]
        self.sift_down(0)
        return min_val

    def print(self):
        print('---STRUCTURE START---')
        size = len(self)
        if size > 0:
            for i in range(0, int(math.log2(size)) + 1):
                for j in range(2**i-1, min(2**(i+1)-1, size)):
                    print(self.__heap[j], end=' ')
                print()
        print('---STRUCTURE END---')

    def min(self):
        return self.__heap[0]

    def sift_up(self, index: int):
        if index != 0:
            p_index = (index - 1) // 2
            if self.__heap[p_index] > self.__heap[index]:
                self.__heap[p_index], self.__heap[index] = self.__heap[index], self.__heap[p_index]
                self.sift_up(p_index)

    def sift_down(self, index: int):
        if index * 2 + 1 < len(self):
            left = index * 2 + 1
            right = index * 2 + 2
            min_ind = left
            if right < len(self) and self.__heap[right] < self.__heap[left]:
                min_ind = right
            if self.__heap[index] > self.__heap[min_ind]:
                self.__heap[index], self.__heap[min_ind] = self.__heap[min_ind], self.__heap[index]
                self.sift_down(min_ind)


main()