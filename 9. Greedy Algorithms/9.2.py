from collections import Counter
from typing import List


class Node:
    def __init__(self, w, zero, one, c):
        self.w = w
        self.zero = zero
        self.c = c
        self.one = one


dic = {}


def dfs(x: Node, res: int) -> None:
    if x.zero is None:
        dic[x.c] = res
        return
    res += 1
    dfs(x.zero, res)
    dfs(x.one, res)


def huffman(s: str) -> None:
    a = [0] * 256
    for i in range(0, len(s)):
        a[ord(s[i])] += 1
    q = []
    for i in range(0, 256):
        if a[i] > 0:
            q.append(Node(a[i], None, None, chr(i)))
    if len(q) == 1:
        dic[q[0].c] = 1
        return
    while len(q) > 1:
        q.sort(key=lambda x: x.w, reverse=True)
        t1 = q.pop()
        t2 = q.pop()
        n = Node(t1.w + t2.w, t2, t1, '\0')
        q.append(n)
    dfs(q[0], 0)


def main():
    message = input()
    huffman(message)
    result = 0
    for i in message:
        result += dic[i]
    print(result)


main()