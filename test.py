import random

#Generating random list of marks for each subject
LHin = random.sample (range(0,100), 100)        #List for Hindi
LEng = random.sample (range(0,100), 100)        #List for English
LPhy = random.sample (range(0,100), 100)        #List for Physics
LChe = random.sample (range(0,100), 100)        #List for Chemistry
LMat = random.sample (range(0,100), 100)        #List for Mathematics

#Making a list called "Average" to store the average marks of students
Average = [None]*100
for i in range (0,100):
    Average[i] = (LHin[i] + LEng[i] + LPhy[i] + LChe[i] + LMat[i])/5

#To make grade list of students
Grade = [None]*100
for j in range (0,100):
    if Average[j] >= 80:
        Grade[j] = 'A'
    elif Average[j] < 80 and Average[j] >= 60:
        Grade[j] = 'B'
    elif Average[j] < 60 and Average[j] >= 40:
        Grade[j] = 'C'
    elif Average[j] < 40 and Average[j] >= 30:
        Grade[j] = 'D'
    else:
        Grade[j] = 'F'

#Storing the Grade list in a file
with open ("StudentGrade.txt", 'w', encoding = 'utf-8') as f:
    for item in Grade:
        f.write("%s\n" % item)

