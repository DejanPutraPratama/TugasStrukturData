def fib(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return (fib(n - 1)+ fib(n - 2))

print("Bilangan Fibbonaci ke 5 adalah",fib(5))
print("Bilangan Fibbonaci ke 7 adalah",fib(7))
print("Bilangan Fibbonaci ke 10 adalah",fib(10))

