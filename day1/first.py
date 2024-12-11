list1, list2 = [], []

with open("input.txt", "r") as file:
    for line in file:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

list1.sort()
list2.sort()

output = sum(abs(a - b) for a, b in zip(list1, list2))

print(output)
