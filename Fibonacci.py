from itertools import count


Count = int(input("Enter a number: "))
Fib = []
Fib =[1]
Next = int(1)
Buffer=int(0)
Pre=int(0)
if Count != 1:
    for i in range(Count-1):
        Buffer = Next
        Next = Pre + Next
        Pre = Buffer
        Fib.append(Next)
print(Fib)

