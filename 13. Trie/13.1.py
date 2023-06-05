def main() -> None:
    trie = Trie()
    can_move = True
    while can_move:
        command, *args = input().split()
        if command == "add":
            result = trie.add(args[0])
        elif command == "get":
            result = trie.get(args[0], int(args[1]))
        else:
            result = "bye"
            can_move = False
        print(result)


class Node:
    def __init__(self) -> None:
        self.is_end = False
        self.child = {}

    def get_child(self, i):
        if i not in self.child:
            self.child[i] = Node()
        return self.child[i]


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def get(self, pref: str, count: int) -> str:
        node = self.root
        result_words = []
        for i in pref:
            if i not in node.child:
                return 'empty'
            node = node.child[i]

        self.get_all_children(node, pref, result_words)

        result = []
        for word in result_words:
            if len(word) > len(pref):
                result.append(word)

        result = sorted(result)[:count]
        return ' '.join(result) if len(result) != 0 else "empty"

    def get_all_children(self, node: Node, word: str, result: []) -> None:
        if node.is_end:
            result.append(word)
        for char in node.child.keys():
            self.get_all_children(node.child[char], word + char, result)

    def add(self, s: str) -> str:
        node = self.root
        for i in s:
            node = node.get_child(i)
        node.is_end = True
        return "ok"


main()
