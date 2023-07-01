def tens_matrix(inner_matrix):
    for line in range(len(inner_matrix)):
        for column in range(line+1, len(inner_matrix)):
            inner_matrix[line][column], inner_matrix[column][line] =\
                inner_matrix[column][line], inner_matrix[line][column]


multiplicity = 6
rand_matrix = []
for lines in range(1, multiplicity + 1):
    rand_matrix.append([numb for numb in range(
        (lines - 1) * multiplicity + 1, lines * multiplicity + 1)])

for lines in rand_matrix:
    print(lines)

tens_matrix(rand_matrix)
print()
for lines in rand_matrix:
    print(lines)
