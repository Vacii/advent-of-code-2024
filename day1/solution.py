from collections import Counter

from utils.helpers import load_file_into_arrays

list1, list2 = load_file_into_arrays("day1/input.txt")

list1.sort()
list2.sort()

counter = Counter(list2)

star1 = sum(abs(a - b) for a, b in zip(list1, list2))
star2 = sum(number * counter[number] for number in list1)


print("Star1:", star1)
print("Star2:", star2)
