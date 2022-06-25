# Loop over pandas dataframes
import pandas


student_dict = {
    "student" : ["carlos", "daniel", "dave"],
    "score": [56,76,80]
}
student_df = pandas.DataFrame (student_dict)

print(student_df)

#Loop
# for (key, value) in student_df.items():
#     print(key, value)

#Loop throught rows
for (index , row) in student_df.iterrows():
    print(index, row.student)
