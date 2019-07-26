# -*- coding: utf-8 -*-


def _cut_rope(length: int) -> int:
    '''
        dynamic programming
    '''
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    
    products = [0] * (length + 1)
    products[1] = 1
    products[2] = 2
    products[3] = 3

    for i in range(4, length+1):
        maxVal = 0
        for j in range(1, i//2+1):
            product = products[j] * products[i - j]
            if maxVal < product:
                maxVal = product
            products[i] = maxVal
    return products[-1]


def cut_rope(length: int) -> int:
    '''
        Greedy method
    '''
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    numOf3 = length // 3
    if length - numOf3 * 3 == 1:
        numOf3 -= 1
    numOf2 = (length - numOf3 * 3) // 2
    return  (3 ** numOf3) * (2 ** numOf2)


if __name__ == '__main__':
    print('dynamic programming method:')
    print(_cut_rope(18))
    print(_cut_rope(100))
    print(_cut_rope(10))
    print(_cut_rope(4))  
    print()
    print('greedy method:')
    print(cut_rope(18))
    print(cut_rope(100))
    print(cut_rope(10))
    print(cut_rope(4))
    

