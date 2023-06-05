def main():
    leaves = input().split()
    trie = Trie(leaves)
    while True:
        code = input()
        command, *args = code.split()
        if command == "+":
            trie.add(args[0])
            print("ok")
        elif command == "?":
            word = " "
            if len(args) > 0:
                word = args[0]
            result = trie.find_words(word)
            if result:
                print(result[1:] if word == " " else result)
            else:
                print("None")
        elif command == "exit":
            print("bye")
            break

class Node:
    def __init__(self):
        self.is_end = False
        self.count = 0
        self.child = {}


class Trie:
    def __init__(self, words: []):
        self.root = Node()
        for word in words:
            self.add(word)

    def find_child(self, node: Node, word: str, result):
        if node.is_end:
            result.append((word, node.count))
        for char in node.child.keys():
            self.find_child(node.child[char], word + char, result)

    def node_by_prefix(self, prefix: str) -> Node:
        node = self.root
        if prefix == " ":
            return node
        for i in prefix:
            if i not in node.child:
                return None
            node = node.child[i]
        return node

    def find_words(self, prefix: str) -> str:
        node = self.node_by_prefix(prefix)
        if not node:
            return None
        children = []
        self.find_child(node, prefix, children)
        best_words = get_best_strings(children)
        if len(best_words) > 1:
            best_words.sort(key=lambda word: (len(word), word))
        return best_words[0]

    def add(self, s: str):
        node = self.root
        for i in s:
            if i not in node.child:
                node.child[i] = Node()
            node = node.child[i]
        node.is_end = True
        node.count += 1


def get_best_strings(words: []) -> []:
    max_value = 0
    result = []
    for string, value in words:
        if value > max_value:
            result.clear()
            max_value = value
            result.append(string)
        if value == max_value:
            result.append(string)
    return result


main()