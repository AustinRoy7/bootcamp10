endNumber = int(raw_input("Enter the end number here "))

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print map(fib, range(0, endNumber))