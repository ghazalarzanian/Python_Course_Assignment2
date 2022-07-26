from unittest import result

result = int(0)
while True:
    A = (input("Enter your number or to exit enter exit: "))
    if A == "exit":
        break
    else :
        A = int(A)
        result = int(result+A)
print(result)