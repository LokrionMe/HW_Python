a = 'C:/Education/file.txt'

def split_way(abs_way:str):
    path = abs_way.rsplit('/',maxsplit=1)[0]
    name = abs_way.rsplit('/',maxsplit=1)[1].rsplit('.',maxsplit=1)[0]
    expansion = abs_way.rsplit('/',maxsplit=1)[1].rsplit('.',maxsplit=1)[1]
    return [path, name, expansion]

print(split_way(a))