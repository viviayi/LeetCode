# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:28:36 2019

@author: 11104510

在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。


示例 1：

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L_num = 0
        R_num = 0
        splitStringNum = 0
        for i in range(len(s)):
            if s[i]=='L':
                L_num+=1
            else:
                R_num+=1
            if L_num == R_num:
                splitStringNum += 1
                L_num = 0
                R_num = 0
            elif i == len(s)-1:
                splitStringNum = 1
        return splitStringNum

if __name__ == '__main__':
    sl = Solution()
    print(sl.balancedStringSplit('LLLLRRRR'))