import re

with open('./day3input.txt', "r") as file:
    lines = file.readlines()

puzzle = []

for line in lines:
    puzzle.append(line)

pattern = r"do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)"

matches = [match for text in puzzle for match in re.findall(pattern, text)]

strip_chars = "mul()"
cleaned_matches = [s.strip(strip_chars) for s in matches]

allowed = True
total_sum = 0
for match in cleaned_matches:
    if match == "don't":
        allowed = False
    if match == "do":
        allowed = True
    if ',' in match and allowed == True:
        x, y = map(int, match.split(','))
        total_sum += x * y

print(total_sum)
