def f(n):
    if n == 0:
        return 1
    if n <= 3:
        return 1
    if n == 4:
        return 2
    return f(n-1) + f(n-4)