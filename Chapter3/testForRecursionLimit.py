def foo(n):
    print(n)
    n += 1
    foo(n)


foo(1)