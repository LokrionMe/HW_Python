from os import walk, path
import pickle
import csv
import json


def sum_direct(way):
    dir_sizes = dict()
    for root, dirs, files in walk(way, topdown=False):
        size = sum(path.getsize(path.join(root, f)) for f in files)
        size += sum(dir_sizes[path.join(root, d)] for d in dirs)
        dir_sizes[root] = size
    return size


sum_directs = 0
f_list = [['Name', 'Parent', 'Size', 'Type'],]
for root, directs, files in walk("C:\Education\Python\hw8", topdown=False):
    if files != []:
        sum_files = 0
        for j in files:
            temp_list = []
            temp_list.append(j)
            temp_list.append(root.rsplit('\\', 2)[2])
            file_size = (path.getsize(root + '/' + j))
            temp_list.append(file_size)
            temp_list.append('file')
            f_list.append(temp_list)
            sum_files += file_size
        sum_directs += sum_files
    temp_list = []
    temp_list.append(root.rsplit('\\', 2)[2])
    temp_list.append(root.rsplit('\\', 2)[1])
    temp_list.append(sum_direct(root))
    temp_list.append('folder')
    f_list.append(temp_list)

f_dict = {a[0]: list(a[1::]) for a in list(zip(*[a for a in f_list]))}

with open("data.pickle", "wb") as p_file:
    pickle.dump(f_dict, p_file)
    print("Pickle file is created")

with open("data.csv", "w", newline="") as csv_file:
    csvfile = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    csvfile.writerow(f_dict.keys())
    for i in range(len(f_dict[list(f_dict.keys())[0]])):
        f_list = []
        for j in f_dict.keys():
            f_list.append(f_dict[j][i])
        csvfile.writerow(f_list)
    print("CSV file is created")

with open("data.json", "w") as write_file:
    json.dump(f_dict, write_file)
    print("JSON file is created")
