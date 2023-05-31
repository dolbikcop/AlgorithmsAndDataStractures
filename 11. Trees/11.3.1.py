import sys
from collections import deque


def main():
    start_numbers = int(sys.stdin.readline())
    final_numbers = int(sys.stdin.readline())
    slots = 10 ** (len(str(start_numbers)) - 1)
    combo = {start_numbers: start_numbers}
    visit = deque()
    visit.append(start_numbers)

    while len(visit) != 0 and final_numbers not in combo.keys():
        current_number = visit.popleft()
        if current_number // slots != 9:
            first = current_number + slots
            if first not in combo.keys():
                combo[first] = current_number
                visit.append(first)

        if current_number % 10 != 1:
            last = current_number - 1
            if last not in combo.keys():
                combo[last] = current_number
                visit.append(last)

        right = current_number // 10 + slots * (current_number % 10)
        if right not in combo.keys():
            combo[right] = current_number
            visit.append(right)

        left = current_number % slots * 10 + current_number // slots
        if left not in combo.keys():
            combo[left] = current_number
            visit.append(left)
    final_combo = [final_numbers]
    parent = final_numbers
    while combo[parent] != parent:
        final_combo.append(combo[parent])
        parent = combo[parent]
    print(*reversed(final_combo), sep='\n')


main()
