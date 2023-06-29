def q1(library: dict[str, set]) -> set:
    x: set = set()
    for sets in library.values():
        x = x.union(sets)
    return x


def q2(library: dict[str, set]) -> dict:
    outter_list = []
    lib_set = q1(library)
    all_list = []
    for item in library.values():
        for val in item:
            all_list.append(val)
    for item in lib_set:
        if all_list.count(item) == 1:
            outter_list.append(item)
    outter_lib: dict = {}
    for item in outter_list:
        for key, value in library.items():
            if item in value:
                if key in outter_lib.keys():
                    outter_lib[key].append(item)
                else:
                    outter_lib[key] = [item]
    return outter_lib


def q3(library: dict[str, set]) -> dict:
    outter_list = []
    lib_set = q1(library)
    all_list = []
    for item in library.values():
        for val in item:
            all_list.append(val)
    for item in lib_set:
        if all_list.count(item) == len(library.keys())-1:
            outter_list.append(item)
    outter_lib: dict = {}
    for item in outter_list:
        for key, value in library.items():
            if item not in value:
                if key in outter_lib.keys():
                    outter_lib[key].append(item)
                else:
                    outter_lib[key] = [item]
    return outter_lib


lib: dict[str, set] = {}
lib["vasya"] = {"frying pan", "matches", "tent"}
lib["petya"] = {"matches", "knife", "fire"}
lib["vanya"] = {"matches", "knife"}

print(f"All friends have {', '.join(q1(lib))}")
for key, val in q2(lib).items():
    print(f"Only {key} has {', '.join(val)}")
for key, val in q3(lib).items():
    print(f"Only {key} has not {', '.join(val)}")
