from utils.helpers import load_file_line_by_line_int


def is_safe_line(line):
    sort_side = 1 if line[0] > line[1] else 0
    prev_num = line[0]

    for _, number in enumerate(line[1:], start=1):
        if (sort_side == 0 and number < prev_num) or (
            sort_side == 1 and number > prev_num
        ):
            return False
        if abs(prev_num - number) < 1 or abs(prev_num - number) > 3:
            return False
        prev_num = number

    return True


def is_safe_line_with_dampener(line):
    for i in range(len(line)):
        temp_line = line[:i] + line[i + 1 :]
        if is_safe_line(temp_line):
            return True
    return False


lines = load_file_line_by_line_int("day2/input.txt")

number_of_safe = sum(1 for line in lines if is_safe_line(line))

number_of_safe_with_dampener = sum(
    1 for line in lines if is_safe_line_with_dampener(line)
)

print("Star1:", number_of_safe)
print("Star2:", number_of_safe_with_dampener)
