from pathlib import Path


def load_file_into_arrays(file_name):
    file_path = Path(file_name).resolve()
    list1, list2 = [], []
    with file_path.open("r") as file:
        for line in file:
            a, b = line.split()
            list1.append(int(a))
            list2.append(int(b))
    return list1, list2
