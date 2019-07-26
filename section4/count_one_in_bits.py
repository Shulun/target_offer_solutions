# -*- coding: utf-8 -*-


def numbOf1(n: int) -> int:
    '''
        n & (n - 1) will remove the rightmost one in n
    '''
    count = 0
    while n:
        count += 1
        n = n & (n - 1)
    return count
    


if __name__ == '__main__':
    print(numbOf1(9))
    print(numbOf1(999))
    # print(numbOf1(-9))
    # only works for positive number
    # since Python stores negative numbers 
    # in bits differently
    print(bin(9))
    print(bin(999))
    print(all(bin(n).count('1')==numbOf1(n) for n in range(30)))
    print(all(bin(n).count('1')==numbOf1(n) for n in range(300)))
