#Que.01:

#Write a Python function that takes list of dictionaries representing students'grades (keys: 'name' and 'grade') and returns 
#dictionary where keys are grade levels ('A', 'B', 'C') and the values are the counts of students who received each grade.

def count(students):
    gradescore={'A':0,'B':0,'C':0,'D':0}
    for student in students:
        grade=student['grade']

        if grade>=90:
            gradescore['A']+=1
        elif grade>=80:
            gradescore['B']+=1
        elif grade>=70:
            gradescore['C']+=1
        else:
            gradescore['D']+=1

    return gradescore

students = [
    {'name': 'Dev', 'grade': 58},
    {'name': 'Anisha', 'grade': 71},
    {'name': 'Roshani', 'grade': 82},
    {'name': 'Datta', 'grade': 64},
    {'name': 'Ira', 'grade': 44}
                                    ]

gradescore=count(students)
print("Grades are:",gradescore)