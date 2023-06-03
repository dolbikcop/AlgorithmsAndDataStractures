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


class Heap(Sized):
    def __init__(self):
        self.__heap: List[int] = []

    def __len__(self) -> int:
        return len(self.__heap)

    def append(self, other: int):
        self.__heap.append(other)
        self.sift_up(len(self) - 1)

    def min(self):
        return self.__heap[0]

    def sift_up(self, index: int):
        if index != 0:
            p_index = (index - 1) // 2
            if self.__heap[p_index] > self.__heap[index]:
                self.__heap[p_index], self.__heap[index] = self.__heap[index], self.__heap[p_index]
                self.sift_up(p_index)

main()