from typing import List


def main():
    not_exit = True
    while not_exit:
        command = input().split()
        if len(command) == 0:
            not_exit = False
        elif len(command) == 1:
            pass # add
        else:
            pass # get

class Node:
    def __init__(self):
        self.alphabet = [0] * 256
        self.is_end = False

    def get_child(self, symbol: str):
        index = ord(symbol)
        if self.alphabet[index] == 0:
            self.alphabet[index] = Node()
        return self.alphabet[index]

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word: str):
        child = self.root
        for i in word:
            child = child.get_child(i)
        child.is_end = True

    def print_child(self, word: str, count: int):
        c_node = self.root
        for i in word:
            c_node = c_node.get_child(i)

        while count != 0:
            for i in range(0, 256):
                if c_node.alphabet[i] != 0:
                        c_node.
    def __print_child(self, results: List[str], word: List[str], count: int, node):
        if node != 0:
            
