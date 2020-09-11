#Program to print Fibonacci Series

def FibonacciSeries(num):
    a = 0
    b = 1
    if num == 0:
        return a
    else:
        print("Fibonacci Series upto", num, "is")
        for i in range(0, num):
            c = a + b
            a = b
            b = c
            print(c)

num = int(input("Enter the term"))
FibonacciSeries(num)
