from itertools import product, combinations


def check(array_coord):
    for i in range(len(array_coord)-1):
        for j in range(i+1, len(array_coord)):
            x1 = int(array_coord[i][0])
            x2 = int(array_coord[j][0])
            y1 = int(array_coord[i][1])
            y2 = int(array_coord[j][1])
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True


def field(array_coord):
    for line in range(1, 9):
        for row in range(1, 9):
            a = (line, row)
            if a in array_coord:
                print("X", end="")
            else:
                print("_", end="")
        print()


def queen_varints(queen_amount):
    list_coord = list((i, j) for i, j in product(range(1, 9), repeat=2))
    list_all_variants = combinations(list_coord, queen_amount)
    list_ideal_position = []
    amount_ideal_position = 0
    while amount_ideal_position != 4:
        variant = next(list_all_variants)
        if check(variant):
            print('+')
            list_ideal_position.append(variant)
            amount_ideal_position += 1
    return list_ideal_position
