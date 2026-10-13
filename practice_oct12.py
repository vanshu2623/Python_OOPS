# Task 4
student_marks_db = {1: [78, 88, 69], 2: [67, 89, 91], 3: [77, 81, 92]}

# 1. Average marks
averages = {}

for student_id, marks in student_marks_db.items():
    avg = sum(marks) / len(marks)
    averages[student_id] = avg
    print(f"Student {student_id}: Average Marks = {avg:.2f}")

# 2. Overall topper
topper = 0
for id in averages:
    if averages[id] > averages.get(topper, 0):
        topper = id

print("Congratulations Student", topper, "for being the Overall Topper!")

# 3. Subject-wise topper
for i in range(3):
    highest = 0
    for id, marks in student_marks_db.items():
        if marks[i] > highest:
            highest = marks[i]
            topper = id

    print("Subject", i + 1, "Topper: Student", topper, "Marks:", highest)


# Task 1
data = [1, [2, 3], [4, [5, 6]], 7]
result = []

for i in data:
    if isinstance(i, list):
        for j in i:
            if isinstance(j, list):
                for k in j:
                    result.append(k)
            else:
                result.append(j)
    else:
        result.append(i)

print(result)


# Task 2
input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def new_list(lst):
    output_list = []

    for i in lst:
        output_list.extend(i)

    return output_list

print(new_list(input_list))


# Task 3
l = [8, 8, 6, 4, 3, 4, 5, 7, 3, 4, 6, 7, 5]
new_unique_list = []
for item in l:
    if item not in new_unique_list:
        new_unique_list.append(item)

print(new_unique_list)

# Task 3
lst = [8, 8, 6, 4, 3, 4, 5, 7, 3, 4, 6, 7, 5]
dictionary = {}
for i in lst:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

print(dictionary)    


# Task 3
l = [8, 8, 6, 4, 3, 4, 5, 7, 3, 4, 6, 7, 5]
def remove_duplicate(l):
    new_unique_list = []
    for n in l:
        if n not in new_unique_list:
            new_unique_list.append(n)
    return new_unique_list

nl = remove_duplicate(l)

freq = {}
for i in nl:
    freq[i] = l.count(i)

print("nl =", nl)
print("freq =", freq)


