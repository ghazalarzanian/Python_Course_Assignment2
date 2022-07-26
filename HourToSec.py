Clock = input("Enter Clock like this 00:00:00  :")
Hour =int (Clock[0:2]) 
Hour = Hour*3600
Min =int (Clock[3:5])
Min = Min *60
Sec = int(Clock[6:8])
Total = int(Hour + Min +Sec)
print (Total)