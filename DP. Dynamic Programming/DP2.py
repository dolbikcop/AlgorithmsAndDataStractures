class Cake:
    def __init__(self, price: int, weight: int, can_slice: bool):
        self.price = price
        self.weight = weight
        self.density = price / weight
        self.can_slice = can_slice

    def __gt__(self, other):
        return self.density > other.density

    def __le__(self, other):
        return self.density <= other.density

    def __ge__(self, other):
        return self.density >= other.density

    def __lt__(self, other):
        return self.density < other.density

def main():
    cakes = []
    n, bag = map(int, input().split())
    for i in range(n):
        p, w, slice = input().split()
        cakes.append(Cake(int(p), int(w), slice == 'Д'))

    cakes.sort()

    final_price = 0.0
    while len(cakes) > 0 and bag > 0:
        cake = cakes.pop()
        if cake.weight <= bag:
            bag -= cake.weight
            final_price += cake.price
        else:
            if cake.can_slice:
                final_price += cake.density * bag
                bag = 0
    print(f'{final_price:.2f}')

main()
