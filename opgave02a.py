
def fib(n):
    a = 0
    b = 1
    cur = a + b
    i = 2
    while i <= n:
        cur = a+b
        a, b = b, a+b
        i += 1
    return cur


def rfib(n):
    if n <= 1:
        return n
    return rfib(n-1) + rfib(n-2)


def main():
    print(rfib(0), fib(0))
    print(rfib(1), fib(1))
    print(rfib(2), fib(2))
    print(rfib(3), fib(3))
    print(rfib(4), fib(4))
    print(rfib(5), fib(5))
    print(rfib(6), fib(6))
    print(rfib(7), fib(7))
    print(rfib(8), fib(8))
    print(rfib(9), fib(9))


if __name__ == '__main__':
    main()
