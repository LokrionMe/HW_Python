import csv
import pickle

with open("data.csv", "r", newline='') as r_csv:
    reader = csv.reader(r_csv, quoting=csv.QUOTE_NONNUMERIC)
    f_list = []
    for row in reader:
        f_list.append(row)
    print("CSV file is read")

f_dict = {a[0]: list(a[1::]) for a in list(zip(*[a for a in f_list]))}

with open("data2.pickle", "wb") as p_file:
    pickle.dump(f_dict, p_file)
    print("Pickle file is created")

with open("data2.pickle", "rb") as p_file:
    r_pickle: dict = pickle.load(p_file)
    print("Pickle file is read")

print(r_pickle)
