# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:16:24 2019

@author: 11104510

实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

if __name__ == '__main__':
    sl = Solution()
    print(sl.toLowerCase('Hello'))
    