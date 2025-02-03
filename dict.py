import analysis as data

#Making a student dictionary where information is stored for analysis
student_dict = {}

#Opening the textfiles to fetch the no of lines and storing it in a variable
with open("rolls.txt",'r') as lines:
    num_of_lines = lines.readlines()
    line = len(num_of_lines)

#user has the option to make detailed analysis about Previous data. User can also create new data and erase
#previous ones and rewrite new
print("1. Import previous data\n2. Enter new data")
option = input("Enter your choice:    ")

#What will happen if user selects the first option
if option == '1':

    #Making a list of roll numbers stored in the text file
    roll_list = []
    with open('rolls.txt','r') as roll_num:
        for add in range(line):
            roll = roll_num.readline()
            #Removing '\n' from each element
            roll = roll.replace('\n','')
            roll_list.append(int(roll))

    #Making a list of marks numbers stored in the text file
    marks_list = []
    with open('marks.txt','r') as _marks_:
        for add in range(line):
            marks = _marks_.readline()
            #Removing '\n' from each element
            marks = marks.replace('\n','')
            marks_list.append(float(marks))

    #Making a list of class stored in the text file
    class_list = []
    with open('class.txt','r') as _class_:
        for add in range(line):
            student_class = _class_.readline()
            #Removing '\n' from each element
            student_class = student_class.replace('\n','')
            class_list.append(int(student_class))

    #Making a list of student names stored in the text file
    student_names = []
    with open("names.txt","r") as names:
        for add in range(line):
            name = names.readline()
            #Removing '\n' from each element
            name = name.replace('\n','')
            student_names.append(name)

    #Combining each of the element in student_dict
    #Making keys of roll numbers
    element = 0
    for key in roll_list:
        student_dict[key] = [student_names[element],class_list[element],marks_list[element]]
        element += 1

    data.analysis(student_dict)
    








