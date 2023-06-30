#не понял задание 

def inner_key(*, key)->dict:
    print(globals()[key])
    lib[globals()[key]] = str(key)

lib = {}
a = 'hi'
inner_key(key=a)
print(lib)