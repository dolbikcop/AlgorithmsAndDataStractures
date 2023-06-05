def main():
    n = int(input())
    trie = Trie()
    for i in range(n):
        banned = input().lower()
        trie.add(banned)

    m = int(input())
    ban = False
    count_line = -1
    symbol = -1
    for i in range(m):
        line = input().lower()
        if ban:
            continue
        words = line.split(" ")
        count = 0
        for word in words:
            correctness = trie.check_word(word)
            if correctness != -1:
                ban = True
                count_line = i + 1
                symbol = count + 1 + correctness
                break
            count += len(word) + 1

    if not ban:
        print("Одобрено")
    else:
        print(f"{count_line} {symbol}")


class Node:
    def __init__(self):
        self.is_end = False
        self.child = {}

    def get_child(self, i):
        if i not in self.child:
            self.child[i] = Node()
        return self.child[i]


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, s: str):
        node = self.root
        for i in s:
            node = node.get_child(i)
        node.is_end = True

    def check_word(self, s: str) -> int:
        word = self.root
        correctness = 0
        for i in s:
            if i not in word.child:
                word = self.root
                correctness += 1
                continue

            word = word.child[i]
            if word.is_end:
                break

        return -1 if not word.is_end else correctness


main()
