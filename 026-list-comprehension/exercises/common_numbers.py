

with open("file1.txt", "r") as file1:
    list1 = file1.readlines()

with open("file2.txt", "r") as file2:
    list2 = file2.readlines()

common_numbers = [int(n) for n in list1 if n in list2]
print(common_numbers)

 