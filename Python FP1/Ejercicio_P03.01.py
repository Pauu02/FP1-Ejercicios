def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return None
    else:
        sol = 1
        while n > 1:
            sol = sol * n
            n = n-1
        return sol


if "__main__" == __name__:
    n1 = 0
    n2 = 5
    n3 = -2

    print(factorial(n1))
    print(factorial(n2))
    print(factorial(n3))
