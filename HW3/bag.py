from itertools import combinations


def maximum_weight(max_weigt:float):
    dict_bag:dict[str, float] = {"tent": 12, "matches": 0.5,
                "water": 5, "knife": 2.5, "axe": 3, "cup": 1.2}
    outter_list = []
    for i in range(1, len(dict_bag.values()) + 1):
        list_combinations = list(combinations(dict_bag.keys(), i))
        for combin in list_combinations:
            delta_weight = max_weigt
            for item in combin:
                delta_weight = delta_weight - dict_bag[item]
            if delta_weight >= 0:
                outter_list.append(combin)
    return outter_list


print(maximum_weight(12))
