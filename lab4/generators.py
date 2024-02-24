#ex1
def squares():
    n=int(input())
    a=(int(i)**2 for i in range(0,n))
    for i in range(n):
        print(next(a))
#ex2
def evens():
    n=int(input())
    a=(int(i) for i in range(0, n, 2))
    for i in range(int(n/2)):
        print(next(a), end = ", ")
    print(next(a))

#ex3
def divisible_by_three_and_four(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in divisible_by_three_and_four(n):
    print(num)

#ex4
def squaresFromAtoB():
    a = int(input())
    b = int(input())
    gen = (int(i)**2 for i in range(a, b + 1))
    for i in range((b-a) + 1):
        print(next(gen))

#ex
def decreasing():
    n = int(input())
    a = (i for i in range(n, 0, -1))
    for i in range(n):
        print(next(a))