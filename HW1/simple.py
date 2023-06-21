a = int(input("Input number: "))
if a == 2:
    print("simple")
elif a % 2 == 0:
    print("not simple")
else:
    c = int(a ** 0.5)
    for i in range(2, c):
        if a % i == 0:
            print("not simple")
            exit()
    print("simple")
