from fractions import Fraction


def finding_nod(x: int, y: int) -> int:
    nod = 1
    x = abs(x)
    y = abs(y)
    while x > 0:
        if x > y:
            x = x % y
            nod = y
        else:
            y = y % x
            nod = y
    return nod


def common_denominator(x: int, y: int) -> int:
    return x*y


def mult_factions(x: list[int], y: list[int]) -> str:
    numerator = x[0]*y[0]
    denominator = common_denominator(x[1], y[1])
    nod = finding_nod(numerator, denominator)
    return str(int(numerator/nod)) + "/" + str(int(denominator/nod))


def sum_factions(x: list[int], y: list[int]) -> str:
    if x[1] != y[1]:
        numerator = x[0]*y[1]+y[0]*x[1]
        denominator = common_denominator(x[1], y[1])
    else:
        numerator = x[0]+y[0]
        denominator = x[1]
    nod = finding_nod(numerator, denominator)
    return str(int(numerator/nod)) + "/" + str(int(denominator/nod))


i: str = input("Input 1-st fraction: ")
j: str = input("Input 2-nd fraction: ")
a: list[int] = list(map(int, i.split("/")))
b: list[int] = list(map(int, j.split("/")))
print(f"{i} * {j} = {mult_factions(a, b)}")
print(f"{i} + {j} = {sum_factions(a, b)}")
f_one = Fraction(i)
f_two = Fraction(j)
print(f"{f_one} * {f_two} = {f_one * f_two}")
print(f"{f_one} + {f_two} = {f_one + f_two}")
