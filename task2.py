def grade_calc(marks,final_marks):
    if((marks[0] == 0 and marks[1] == 0) or (marks[0] == 0 and marks[2] == 0) or (marks[1] == 0 and marks[2] == 0)):   #  If two or more assessments are awarded zero
        if(final_marks <= 44):     # final mark is between 0 and 44 
            grade = 'AF'
    elif(final_marks <= 44):
        grade = 'F'
    elif(marks[0] != 0 and marks[1] != 0 and marks[2] != 0):   # They do not have any assessment marked zero.
        if(final_marks >= 45 and final_marks <= 49):     # Their final mark is between 45 – 49 (inclusive).
            if((marks[0] < 50 and marks[1] < 50) or (marks[1] < 50 and marks[2] < 50) or (marks[0] < 50 and marks[2] < 50)):    # They only failed (i.e., less than 50) one assessment.
                grade = 'F'
            elif((marks[0] < 50 and marks[1] > 50) or (marks[0] > 50 and marks[1] < 50)):  # they failed is Assessment 1 or Assessment 2
                grade = 'SA'
            elif(marks[2] < 50):
                 grade = 'SE'      
        elif(final_marks >= 50 and final_marks <= 64):
            grade = 'P'
        elif(final_marks >= 65 and final_marks <= 74):
            grade = 'C'
        elif(final_marks >= 75 and final_marks <= 84):
            grade = 'D'
        elif(final_marks >= 85):
            grade = 'HD'
    elif((marks[0] == 0 or marks[1] == 0 or marks[2] == 0) and final_marks >= 45 and final_marks <= 49):
        grade = 'F'
    return grade

def count_grades(dict1):
    hd,d,c,p,sp,f,af=0,0,0,0,0,0,0
    for a in dict1.keys():
        grade=dict1[a][4]
        if grade=='HD':
            hd+=1
        elif grade=='D':
            d+=1
        elif grade=='C':
            c+=1
        elif grade=='P':
            p+=1
        elif grade=='SP':
            sp+=1
        elif grade=='F':
            f+=1
        elif grade=='AF':
            af+=1
    return (hd,d,c,p,sp,f,af)

def average(dict1):
    avg_marks1,avg_marks2,avg_marks3,avg_marks4,avg_point=0,0,0,0,0
    for a in dict1.keys():
        avg_marks1+=dict1[a][0]
        avg_marks2+=dict1[a][1]
        avg_marks3+=dict1[a][2]
        avg_marks4+=dict1[a][3]
        grade=dict1[a][4]
        if grade=='HD':
            avg_point+=4.0
        elif grade=='D':
            avg_point+=3.0
        elif grade=='C':
            avg_point+=2.0
        elif grade=='P':
            avg_point+=1.0
        elif grade=='SP':
            avg_point+=0.5
        elif grade=='F':
            avg_point+=0.0
        elif grade=='AF':
            avg_point+=0.0
    avg_marks1/=len(dict1.keys())
    avg_marks2/=len(dict1.keys())
    avg_marks3/=len(dict1.keys())
    avg_marks4/=len(dict1.keys())
    avg_point/=len(dict1.keys())
    return (avg_marks1,avg_marks2,avg_marks3,avg_marks4,avg_point)

count=1
dict1={}
while True:
    marks = input("Enter a student’s assessment marks (separated by comma), type in letter N to finish: ")
    if marks=='N':
        break
    marks = [float(item) for item in  marks.split(',')]
    final_marks = int((marks[0] * 0.2 + marks[1] * 0.4 + marks[2] * 0.4) + 0.5)
    grade=grade_calc(marks,final_marks)
    marks.append(final_marks)
    marks.append(grade)
    if grade=='SA' or grade=='SE':
        supp_marks=float(input("What is this student’s supplementary assestment mark: "))
        marks.append(supp_marks)
        if supp_marks>50:
            marks[4]='SP'
        else:
            marks[4]='F'
    dict1[count]=marks
    count+=1
    
num_stud=count-1
count_grade=count_grades(dict1)
avg=average(dict1)
pass_rate=(count_grade[0]+count_grade[1]+count_grade[2]+count_grade[3]+count_grade[4])/num_stud
adj_pass_rate=(count_grade[0]+count_grade[1]+count_grade[2]+count_grade[3]+count_grade[4])/(num_stud-count_grade[6])
print("Number of students: ",num_stud)
print('Student pass rate: %.2f%%'%round(pass_rate,2))
print('Student pass rate (adjusted): %.2f'%round(adj_pass_rate,2))
print('Average mark for Assessment 1: %.2f'%round(avg[0],2))
print('Average mark for Assessment 2: %.2f'%round(avg[1],2))
print('Average mark for Assessment 3: %.2f'%round(avg[2],2))
print('Average final mark: %.2f'%round(avg[3],2))
print('Average grade point: %.2f'%round(avg[4],2))
print('Number of HDs: ',count_grade[0])
print('Number of Ds: ',count_grade[1])
print('Number of Cs: ',count_grade[2])
print('Number of Ps: ',count_grade[3])
print('Number of SPs: ',count_grade[4])
print('Number of Fs: ',count_grade[5]+count_grade[6])