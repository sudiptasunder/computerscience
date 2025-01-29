import math as m
import statistics as stats

def line():
    print('-'*50)

#This is our student_dict
student_dict = {32:("Sudipta",11,580),34:("Uvy",11,580),35:("Shanta",11,520)}

#Creating a list to store the marks to analyse them
marks_list = []

#Starting to store the marks from student_dict using a for loop
for el in student_dict:
    marks_list.append(student_dict[el][2])

#Finding the max and min marks and then storing them inside variables
search_min = min(marks_list)
search_max = max(marks_list)

#Creating a list to store the keys or roll numbers which have the same min and max marks
min_keylist = []
max_keylist = []

#Finding the keys or roll numbers which have the same min marks
for key in student_dict:
    if search_min == student_dict[key][2]:
        min_keylist.append(key)

#Finding the keys or roll numbers which have the same max marks
for key in student_dict:
    if search_max == student_dict[key][2]:
        max_keylist.append(key)

#Displaying the student with hightest percentage
print("****The student(s) with the highest percentage are as follows****")
for execute in max_keylist:
    line()
    print("Roll Number:    ",execute)
    print("Name:    ",student_dict[execute][0])
    print("Class:    ",student_dict[execute][1])
    print("Percentage:    ",student_dict[execute][2])
    line()

#Displaying the student with lowest perccentage
print("****The student(s) with the minimum percentage are as follows****")
for execute in min_keylist:
    line()
    print("Roll Number:    ",execute)
    print("Name:    ",student_dict[execute][0])
    print("Class:    ",student_dict[execute][1])
    print("Percentage:    ",student_dict[execute][2])
    line()

print("****The average percentage of student(s) are as follows****")
line()
print("No. of student(s) listed:    ",len(marks_list))
print("Maximum percentage:    ",search_max)
print('Minimum percentage:    ',search_min)
print("Average percentage:    ", stats.mean(marks_list))
line()
