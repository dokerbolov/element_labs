


def fibonacciNumber(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fibonacciNumber(num - 1) + fibonacciNumber(num - 2)

a = int(input())

print(fibonacciNumber(a))