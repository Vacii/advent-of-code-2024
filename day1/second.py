from collections import Counter

list1, list2 = [], []

with open("input.txt", "r") as file:
    for line in file:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

list1.sort()

counter = Counter(list2)

output = sum(number * counter[number] for number in list1)

print(output)
