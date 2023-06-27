
def find_double(inner_list: list) -> list:
    outer_list = []
    for item in set(inner_list):
        if inner_list.count(item)>1:
            outer_list.append(item)
    return outer_list

random_list = ['a', 'b', 'c', 'a', 1, 2, 3, 1, 1, 1]
print(find_double(random_list))
