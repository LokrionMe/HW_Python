a: int = int(input("Input integer number: "))
lib: dict[int, str] = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
list_numbers: list[str] = []
BASIS: int = 16
print(hex(a))
while a > 0:
    if a % 16 == 0:
        list_numbers.append("0")
    elif a > BASIS:
        if a % BASIS > 9:
            list_numbers.append(lib[a % BASIS])
        else:
            list_numbers.append(str(a % BASIS))
    elif 9 < a < 16:
        list_numbers.append(lib[a])
    else:
        list_numbers.append(str(a))
    a = a // BASIS
print("0x"+"".join(list_numbers[::-1]))
