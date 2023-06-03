def main():
    heap = Heap()
    n, bag = map(int, input().split())
    for i in range(n):
        p, w = map(int, input().split())
        heap.append(Cake(p, w))

    final_price = 0.0
    while heap.get_size() > 0 and bag > 0:
        cake = heap.max()
        if cake.weight <= bag:
            heap.pop()
            bag -= cake.weight
            final_price += cake.price
        else:
            final_price += cake.density * bag
            bag = 0
    print(f'{final_price:.2f}')


class Cake:
    def __init__(self, price: int, weight: int):
        self.price = price
        self.weight = weight
        self.density = price / weight

    def __gt__(self, other):
        return self.density > other.density

    def __le__(self, other):
        return self.density <= other.density

    def __ge__(self, other):
        return self.density >= other.density

    def __lt__(self, other):
        return self.density < other.density


class Heap():
    def __init__(self):
        self.array = []

    def get_size(self):
        return len(self.array)

    def append(self, other):
        self.array.append(other)
        self.sift_up(len(self.array) - 1)

    def pop(self):
        min_val = self.array[0]
        size = len(self.array) - 1
        self.array[0] = self.array[size]
        self.array.pop()
        self.sift_down(0)
        return min_val

    def max(self):
        return self.array[0]

    def sift_up(self, index: int):
        if index != 0:
            p_index = (index - 1) // 2
            if self.array[p_index] < self.array[index]:
                self.array[p_index], self.array[index] = self.array[index], self.array[p_index]
                self.sift_up(p_index)

    def sift_down(self, index: int):
        if index * 2 + 1 < len(self.array):
            left = index * 2 + 1
            right = index * 2 + 2
            min_ind = left
            if right < len(self.array) and self.array[right] > self.array[left]:
                min_ind = right
            if self.array[index] < self.array[min_ind]:
                self.array[index], self.array[min_ind] = self.array[min_ind], self.array[index]
                self.sift_down(min_ind)


main()
