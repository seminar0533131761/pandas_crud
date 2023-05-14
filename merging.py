import pandas as pd

from options import Options


# index_col=None on reading csv file
# access students and final answer by final answer
def merging_answer():
    d = pd.read_csv("desires.csv")
    s = pd.read_csv("students.csv")
    merged_df = pd.merge(s, d, on='id')
    filtered_df = merged_df[merged_df['answer'] == "math"]
    # filtered_df.to_csv('filtered_data.csv', index=False)
    # f=pd.read_csv('filtered_data.csv')
    ls = filtered_df.T.to_dict().values()
    print(list(ls))


def how_many_on_each_trainig():
    d = pd.read_csv("desires.csv")
    count_students_in_each_opt = dict()
    for opt in Options:
        name = opt.name
        sum_per_opt = (d['answer'] == name).sum()
        mew_value = {name: int(sum_per_opt)}
        count_students_in_each_opt.update(mew_value)
    opts_name = list(count_students_in_each_opt.keys())
    opts_sum = list(count_students_in_each_opt.values())
    print(opts_sum)
    print(opts_name)


def student_grade():
    g = pd.read_csv("grades.csv",index_col=None)
    student1=g[(g['id'] ==1)]
    student2 = g[(g['id'] == 2)]
    subjects = list(g.columns)
    student1_grades=student1.to_dict().values()
    # Access values of the dictionaries as lists
    lst=[list(i.values()) for i in student1_grades]
    print(lst)
    nw_lst=[int(i[0]) for i in lst]
    print(nw_lst)
    # for data_dict in data_list:
    #     values = list(data_dict.values())
    #     print(values)

    # print(student1_grades)
    # lst=[i.values() for i in student1_grades]
    #
    # a=list(lst[0])
    # print(a)
    # print(a[0])
    # grades1=list(student1_grades.)
    # print(student1_grades,type(student1_grades))
    # two_students_grades=list()
    # counter=0
    # for student_grade in students_grades:
    #     if counter==2:
    #         break
    #     two_students_grades.append(list(student_grade.values()))
    # print(two_students_grades)



# enum and check if parameter not in the enum
# from enum import Enum
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
#
# # Check if a color is in the enum
# color = "RED"
# if color in Color.__members__:
#     print(f"{color} is a valid color in the enum.")
# else:
#     print(f"{color} is not a valid color in the enum.")
student_grade()
