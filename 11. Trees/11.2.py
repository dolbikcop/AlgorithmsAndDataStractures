import ast
from typing import Dict, List


def get_tree(a: str) -> Dict[int, List[int]]:
    return ast.literal_eval(a)


def get_first_common_element(first_array: List[int], second_array: List[int]):
    for i in reversed(first_array):
        for j in reversed(second_array):
            if i == j:
                return i


def get_parent(tree: Dict[int, List[int]], value: int, key: int, parents: List[int]) -> List[int]:
    if key not in tree:
        return None
    if value in tree[key]:
        return parents
    for i in tree[key]:
        kids = get_parent(tree, value, i, parents + [i])
        if kids is not None:
            return kids


def main():
    n = input()
    v = get_tree(input())
    x, y = map(int, input().split())

    root_item = list(v.keys())[0]
    parents_x = get_parent(v, x, root_item, [root_item])
    parents_y = get_parent(v, y, root_item, [root_item])

    c = get_first_common_element(parents_x, parents_y)

    if c is not None:
        print(c)
    elif len(parents_x) == 0:
        print(x)
    else:
        print(y)


main()
