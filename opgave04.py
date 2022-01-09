def wonder_successor(n):
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    return n


def wonder(n):
    ret = [n]
    while n != 1:
        n = wonder_successor(n)
        ret.append(n)
    return ret


def main():
    print(wonder(27))


if __name__ == '__main__':
    main()
