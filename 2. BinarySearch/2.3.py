from math import sqrt

def solve_full(a: int, v1: int, v2: int, x: int):
    return (sqrt((1-a)*(1-a) + x*x) / v1) + (sqrt((1-x)*(1-x) + a*a) / v2)

def main():
    v1, v2 = map(int, input().split())
    a = 1 - (int(input()) / 100)
    left = 0
    right = 1
    eps = 0.0000000005
    while(abs(right - left) > eps):
        middle = (left + right) / 2
        left_val = solve_full(a, v1, v2, middle-eps)
        right_val = solve_full(a, v1, v2, middle+eps)
        if (left_val < right_val):
            right = middle
        else:
            left = middle
    print('%.6f' % round(middle, 6))

if __name__ == '__main__':
    main()