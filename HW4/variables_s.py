def kill_s():
    lib = dict(globals())
    for x, y in lib.items():
        if "s" == x[-1] and len(x) != 1:
            globals()[f'{x[0:-1:]}'] = y
            globals()[f'{x}'] = None


items = 2
b = 9
s = 'hi'
phones = [1, 2, 3]

print(items)
print(s)
print(phones)
print(b)

kill_s()

print()
print(items)
print(item)
print(s)
print(phones)
print(phone)
print(b)
