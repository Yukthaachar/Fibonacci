def find_fibonacci():
    def fib(n):
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return fib(n-1)+fib(n-2)
    fibonacci =[]    
    for i in range(1,11,1):    
        fibonacci.append(fib(i))
    return fibonacci