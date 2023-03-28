import sys

def main():
    sys.stdin.readline()
    plates = sys.stdin.readline().split()

    for i in range(len(plates)):
        if i > len(plates) / 2:
            break
        plates_before = plates[:i][::-1]
        plates_after = plates[i:i * 2]

        if plates_before == plates_after:
            print(len(plates) - i, end=' ')
main()