from typing import List, Dict

combinations = {}


def main():
    start_numbers = int(input())
    final_numbers = int(input())
    combo = {}
    create_combinations(combo, start_numbers, [start_numbers], final_numbers)
    for i in combo[final_numbers]:
        print(i)


def create_combinations(combo: Dict[int, List[int]], current_number: int, current_combo: List[int], final_number: int):
    if current_number in combo.keys() and len(combo[current_number]) <= len(current_combo):
        return
    if final_number in combo.keys() and len(combo[final_number]) <= len(current_combo):
        return
    if current_number == final_number:
        if current_number not in combo.keys() or len(combo[current_number]) > len(current_combo):
            combo[current_number] = current_combo
        return
    else:
        if current_number not in combo.keys() or len(combo[current_number]) > len(current_combo):
            combo[current_number] = current_combo

        if current_number // 1000 != 9:
            create_combinations(combo, current_number + 1000, current_combo + [current_number + 1000], final_number)
        if current_number % 10 != 1:
            create_combinations(combo, current_number - 1, current_combo + [current_number - 1], final_number)
        right = current_number // 10 + 1000 * (current_number % 10)
        create_combinations(combo, right, current_combo + [right], final_number)
        left = ((current_number % 1000) * 10) + current_number // 1000
        create_combinations(combo, left, current_combo + [left], final_number)


main()
