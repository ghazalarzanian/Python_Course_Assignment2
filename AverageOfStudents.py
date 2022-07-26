from lib2to3.pgen2.token import NUMBER


Number = int(input("Enter number of students : "))
Average = float (0)
Max = float(0)
Min = float(0)
for i in range(Number):
    Score = float(input("Enter the score :"))
    Average += Score
    if Max < Score:
        Max = Score
    if Min > Score:
        Min = Score
Average = Average / Number
print("Average is = ",Average,"The max is :",Max,"The min is : ",Min)