# -*- coding: utf-8 -*-
# Queue: first in first out

class MyQueue1:
    '''
        push: O(1), pop/peek: O(n)
        use one stack to receive data, use another stack to return data
    '''
    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def move(self) -> None:
        if self.out_stack == []:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self.move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return self.in_stack == self.out_stack == []


class MyQueue2:
    '''
        push: O(1), pop/peek: O(1)
    '''
    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        
    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


if __name__ == '__main__':
    q1 = MyQueue1()
    q1.push(1)
    q1.push(2)
    print(q1.peek())
    print(q1.pop())
    print(q1.empty())
    print('--'*10)

    q2 = MyQueue2()
    q2.push(1)
    q2.push(3)
    print(q2.peek())
    print(q2.pop())
    print(q2.peek())
    print(q2.empty())
    print(q2.pop())
    print(q2.empty())


