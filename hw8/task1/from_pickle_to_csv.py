import pickle
import csv

# data отсюда должна совпадать с r_pickle из папки task2
data = {"id": [1, 2, 3, 4, 5],
        "Name": ["Ivan", "Petr", "Maksim", "Nikolay", "Irina"],
        "Age": [18, 19, 21, 24, 19],
        "Sex": ["m", "m", "m", "m", "f"]}

with open("data.pickle", "wb") as p_file:
    pickle.dump(data, p_file)
    print("Pickle file is created")

with open("data.pickle", "rb") as p_file:
    r_pickle: dict = pickle.load(p_file)
    print("Pickle file is read")

with open("data.csv", "w", newline="") as csv_file:
    csvfile = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    csvfile.writerow(r_pickle.keys())
    for i in range(len(r_pickle[list(r_pickle.keys())[0]])):
        f_list = []
        for j in r_pickle.keys():
            f_list.append(r_pickle[j][i])
        csvfile.writerow(f_list)
    print("CSV file is created")
