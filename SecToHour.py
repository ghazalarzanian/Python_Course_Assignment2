A = int(input("Enter time in Sec : "))
Hour = int(A /3600) 
Min = int((A % 3600) / 60)
Sec = int(A - (Hour * 3600) - (Min * 60))
print("Time is :",Hour,":",Min,":",Sec)
