def foo(n):
    n += 1
    print(n)
    foo(n)

if __name__ == "__main__":
    foo(1)
