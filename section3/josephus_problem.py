def lastRemainingSolution(n, m):
    if n <= 0 or m <= 0:
        return -1
    last_num = 0
    for i in range(2, n+1):
        last_num = (last_num + m) % i
    return last_num


print(lastRemainingSolution(100, 3))
print(lastRemainingSolution(100, 4))
print(lastRemainingSolution(100, 5))
print(lastRemainingSolution(123, 3))