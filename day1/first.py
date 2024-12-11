from utils.helpers import load_file_into_arrays

list1, list2 = load_file_into_arrays("day1/input.txt")

list1.sort()
list2.sort()

output = sum(abs(a - b) for a, b in zip(list1, list2))

print(output)
