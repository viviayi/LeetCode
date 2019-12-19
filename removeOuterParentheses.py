# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:41:21 2019

@author: 11104510

有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。

如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。

给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。

对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。

示例 1：

输入："(()())(())"
输出："()()()"
解释：
输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。

"""

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        splitStartIndex = 0
        splitEndIndex = 0
        output = ''
        pair = 0
        for i in range(len(S)):
            if S[i] == '(':
                pair -= 1
            else:
                pair += 1
            if pair == 0:
                splitStartIndex = splitEndIndex
                splitEndIndex = i+1
                output += S[splitStartIndex+1:splitEndIndex-1]
        return output

if __name__ == '__main__':
    sl = Solution()
    print(sl.removeOuterParentheses('(()())(())'))