

def binary_search(legs: [], hands: [], l: int):
    left = 0
    right = l - 1
    max_index = 0
    max_value = 999999
    while left <= right:
        middle = (left + right) // 2
        hands_value = hands[middle]
        legs_value = legs[middle]
        max_now = hands_value if hands_value > legs_value else legs_value
        if max_now < max_value:
            max_index = middle
            max_value = max_now

        if hands_value > legs_value:
            left = middle + 1
        elif hands_value < legs_value:
            right = middle - 1
        else:
            break
    while l > max_index + 1 and \
            max_value\
            == max(hands[max_index + 1], legs[max_index + 1]):
        max_index += 1
    print(max_index)
def main():
    n, m, l = map(int, input().split())
    legs = []
    hands = []
    for i in range(n):
        legs.append(list(map(int, input().split())))
    for i in range(m):
        hands.append(list(map(int, input().split())))
    q = int(input())
    for i in range(q):
        f, s = map(int, input().split())
        binary_search(legs[f], hands[s], l)

main()