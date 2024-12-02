with open('./day1input.txt', "r") as file:
    lines = file.readlines()

column1 = []
column2 = []

for line in lines:
    values = line.strip().split()
    if len(values) == 2:
        column1.append(int(values[0]))
        column2.append(int(values[1]))

column1_sorted = sorted(column1)
column2_sorted = sorted(column2)

sum = 0
for i in range(len(column1_sorted)):
    difference = abs(column1_sorted[i] - column2_sorted[i])
    sum += difference

similarity_sum = 0
for value in column1_sorted:
    count = 0
    for other_value in column2_sorted:
        if value == other_value:
            count += 1
            
    similarity = value * count
    similarity_sum += similarity

print(similarity_sum)








