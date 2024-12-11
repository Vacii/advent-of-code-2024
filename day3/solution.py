import re

data = None
with open("day3/input_test.txt", "r") as file:
    data = file.read().replace("\n", "")

regex = "mul\(\d{1,3},\d{1,3}\)"
regex2 = "\d{1,3}"

x = re.findall(regex, data)
print(x)
star1 = 0
for _, oc in enumerate(x):
    x, y = oc.split(",")
    x_match = re.search(regex2, x)
    y_match = re.search(regex2, y)

    if x_match and y_match:
        x = x_match.group()
        y = y_match.group()
        print(x, y)

        star1 += int(x) * int(y)


print("Star1:", star1)

print("Star2:")
