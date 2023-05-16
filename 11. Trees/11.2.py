import ast


def get_tree_from_str(a: str):
    return ast.literal_eval(a)


print(get_tree_from_str(input()).items())
order = []
first = []
last = []
d = {}
v = []


def dfs2(x, depth, p: int) -> None:
    d[x] = depth
    first[x] = len(order)
    order.append(x)
    for i in range(0, len(v[x])):
        a = v[x][i]
        if a == p:
            continue
        dfs2(a, depth + 1, x)
        order.append(x)
    last[x] = len(order)
    order.append(x)


def get_lca(a, b: int) -> int:
    l = first[a]
    if first[b] < l:
        l = first[b]
    r = last[a]
    if last[b] > r:
        r = last[b]
    ans = 0
    D = d[a]
    for i in range(l, r):
        if d[order[i]] < D:
            ans = order[i]
            D = d[ans]
    return ans
