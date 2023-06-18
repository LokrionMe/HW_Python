for i in range(1, 11):
    for j in range(1, 6):
        if i == 10:
            print(f"{j} x{i}={i*j}", end=" "*3)
        elif i*j > 9:
            print(f"{j} x {i}={i*j}", end=" "*3)
        else:
            print(f"{j} x {i}= {i*j}", end=" "*3)
    print()
print()
for i in range(1, 11):
    for j in range(6, 11):
        if i == 10:
            print(f"{j} x{i}={i*j}", end=" "*3)
        elif i*j > 9:
            print(f"{j} x {i}={i*j}", end=" "*3)
        else:
            print(f"{j} x {i}= {i*j}", end=" "*3)
    print('')
