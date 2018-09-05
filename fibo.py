# Fibonacci numbers module


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# in any file you can import the module, and access the functions that way
import fibo

fibo.fib(5)
fibo.fib2(8)
fibo.__name__

