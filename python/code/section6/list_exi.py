"""
list练习
"""

student_age=[21,25,21,23,22,20]

student_age.append(31)

print(student_age)

new_age=[29,33,30]

student_age.extend(new_age)

print(student_age)

pop_age=student_age.pop(0)

print(pop_age)
print(student_age)

mew1_s=student_age.pop(-1)
print(mew1_s)
print(student_age)

index_age=student_age.index(31)
print(index_age)
