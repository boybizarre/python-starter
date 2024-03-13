import random
import pandas

# numbers = [1, 2, 3]
# new_numbers  = [item + 1 for item in numbers]

# print(new_numbers)

# name = 'Jamal'
# new_list = [letter for letter in name]

# print(new_list)

# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)

# ----- ------- ------ ------ ------ ----- ----- -----


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# print(names)

# new_names = [name.upper() for name in names if len(name) >= 5]
# print(new_names)

# ----- ------- ------ ------ ------ ----- ----- -----


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [num * num for num in numbers]

# print(squared_numbers)

# ----- ------- ------ ------ ------ ----- ----- -----


# list_of_strings = input().split(', ')

# numbers = [int(letter) for letter in list_of_strings]
# odd_numbers = [num for num in numbers if num % 2 == 0]

# print(odd_numbers)


# ----- ------- ------ ------ ------ ----- ----- -----

# with open("file1.txt") as file1:
#     list1 = file1.readlines()

# with open("file2.txt") as file2:
#     list2 = file2.readlines()


# result = [int(num) for num in list1 if num in list2]

# print(result)

# ----- ------- ------ ------ ------ ----- ----- -----


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# student_scores = {student: random.randint(1, 100) for student in names}

# print(student_scores)

# passed_students = {
#     student: score for (student, score) in student_scores.items() if score >= 60
# }

# print(passed_students)


# ----- ------- ------ ------ ------ ----- ----- -----

# sentence = input().split()
# print(sentence)

# result = {word: len(word) for word in sentence}
# print(result)


# ----- ------- ------ ------ ------ ----- ----- -----

# weather_c = eval(input())

# weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}
ÏÏ
# print(weather_c.items())
# print(weather_f)

# ----- ------- ------ ------ ------ ----- ----- -----

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}


# looping through the students
for key, value in student_dict.items():
    print(value)


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # looping through a dataframe
# for key, value in student_data_frame.items():
#     print(key)
#     print(value)


# loop through rows of dataframe
for index, row in student_data_frame.iterrows():
    # print(index)
    # print(row.student)
    if row.student == 'Angela':
        print(row.score)
