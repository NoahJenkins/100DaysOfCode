import pandas

student_dict = {
    "student": ["Ann", "Frank", "Noah"],
    "score": [56,76, 98]
}

import pandas
student_dict_frame = pandas.DataFrame(student_dict)
print(student_dict_frame)

#Loop through a dataframe
# for (key, value) in student_dict_frame.items():
#     print(key)
#     print(value)

#Loop through the rows of a data frame
for (index, row) in student_dict_frame.iterrows():
    print(index)
    print(row)