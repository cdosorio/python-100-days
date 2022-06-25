import random

# LIST Comprehension

# numbers = [1,2,3]
# new_numbers = [item + 1 for item in numbers] 
# print(new_numbers)

# double_range = [item * 2 for item in range(1,5)]
# print(double_range)

#conditional

# lower_numbers = [n for n in range(1,5) if n < 3]
# print(lower_numbers)


names = ["carlos", "daniel", "dave"]
# upper_names = [name.upper() for name in names if len(name) > 3]
# print(upper_names)

######################
# DICT Comprehension

# create dict from list
#new_dict = {new_key: new_value for item in list}
students_scores = {student: random.randint(1,100) for student in names}

# create dict from other dict
#new_dict = {new_key: new_value for (key,value) in dict.items()}
passed_students = {student: score for (student,score) in students_scores.items() if score >= 60}
print(passed_students)





