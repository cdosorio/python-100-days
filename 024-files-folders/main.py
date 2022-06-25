import os

# absolute path
# with open("c:/Users/Acer/Desktop/my_file.txt") as file:
#     content = file.read()
#     print(content)

# relative path 
print(os.path.realpath('../../../../../Desktop'))
print(os.path.realpath('../../../../Desktop'))
print(os.path.realpath('../../../Desktop')) # correct 

with open("../../../Desktop/my_file.txt") as file:
    content = file.read()
    print(content)
    

# #append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nnew text")

# #create if not exists
# with open("my_file2.txt", mode="w") as file:
#     file.write("\nnew text")







