from collections import Counter

def main():
    char_counter = Counter(sorted(list(input())))

    alphabet = map(chr, range(1072, 1104))
    weights = map(int, input().split())
    alphabet_dict = dict(zip(alphabet, weights))

    sign = []
    unsign = []
    sum_elements = 0
    for ch, count in char_counter.items():
        if count >= 2 and alphabet_dict[ch] > 0:
            unsign.extend([ch]*(count-2))
            sign.append(ch)
        else:
            unsign.extend([ch]*count)
    sign = sorted(sign, key=lambda item: (alphabet_dict[item], -ord(item)))
    length = len(unsign)
    for i, ch in enumerate(sign):
        sum_elements += (length+1+i*2) * alphabet_dict[ch]

    print(''.join([*reversed(sign), *unsign, *sign]), sum_elements)

main()