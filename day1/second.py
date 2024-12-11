from collections import Counter

from utils.helpers import load_file_into_arrays

list1, list2 = load_file_into_arrays("day1/input.txt")


list1.sort()

counter = Counter(list2)

output = sum(number * counter[number] for number in list1)

print(output)
