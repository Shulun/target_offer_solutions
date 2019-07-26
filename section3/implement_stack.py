# -*- coding: utf-8 -*-
# Stack: first in last out


from collections import deque


class MyStack:
    '''
        push: O(n), pop/top: O(1)
    '''
    def __init__(self):
        self.q1, self.q2 = deque(), deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


class MyStack2:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # self.q.rotate(1)
        # self.q.rotate(1-len(self.q))
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q


class MyStack3:
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not self.q


if __name__ == '__main__':
    s1 = MyStack()
    s1.push(1)
    s1.push(2)
    print(s1.top())
    print(s1.pop())
    print(s1.top())
    print('--'*10)

    s2 = MyStack2()
    s2.push(1)
    s2.push(2)
    print(s2.top())
    print(s2.pop())
    print(s2.empty())
    print(s2.pop())
    print(s2.empty())
    print('--'*10)

    s3 = MyStack3()
    s3.push(1)
    s3.push(2)
    print(s3.top())
    print(s3.pop())
    print(s3.empty())
    print(s3.pop())
    print(s3.empty())
