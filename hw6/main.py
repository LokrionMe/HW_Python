from queen import queen_varints, field

list_ideal_position = queen_varints(3)
for item in list_ideal_position:
    print(item)
    field(item)
    print()
