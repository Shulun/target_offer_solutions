'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    def replaceSpace1(self, s):
        tempstr = ''
        if not isinstance(s, str):
            return
        for c in s:
            if c == ' ':
                tempstr += '%20'
            else:
                tempstr += c
        return tempstr

    def replaceSpace2(self, s):
        if not isinstance(s, str):
            return
        return s.replace(' ', '%20')

    def replaceSpace3(self, s):
        if not isinstance(s, str) or len(s) <= 0 or s == None:
            return ''
        spaceNum = 0
        for i in s:
            if i == ' ':
                spaceNum += 1

        newStrLen = len(s) + spaceNum * 2 # multiply by 2 because space is already accounted in len(s)
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return ''.join(newStr)

if __name__ == '__main__':
    s = "we are happy"
    test = Solution()
    print(test.replaceSpace1(s))
    print(test.replaceSpace2(s))
    print(test.replaceSpace3(s))
