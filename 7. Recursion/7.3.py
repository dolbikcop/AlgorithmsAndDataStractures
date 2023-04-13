from collections import namedtuple
from typing import List

Dish = namedtuple("Dish", "price calories")


def main():
    count_dish, money = map(int, input().split())
    menu: List[Dish] = []
    for i in range(count_dish):
        price, calories = map(int, input().split())
        menu.append(Dish(price, calories))
    create_meal([], money, 0, 0, menu)
    print(len(global_array), global_count_calorie)
    print(*global_array)


global_count_calorie = 0
global_array = []


def create_meal(arr: List[int], money: int, calories: int, ind: int, menu: List[Dish]):
    if money == 0 or ind == len(menu):
        global global_array, global_count_calorie
        if calories > global_count_calorie or (calories == global_count_calorie and len(arr) > len(global_array)):
            global_array = arr.copy()
            global_count_calorie = calories
    else:
        if menu[ind].price <= money:
            create_meal(arr + [ind+1], money - menu[ind].price, calories + menu[ind].calories, ind + 1, menu)
        create_meal(arr, money, calories, ind+1, menu)


main()
