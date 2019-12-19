# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:19:32 2019

@author: 11104510

两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 2^31.

"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_b = bin(x)
        y_b = bin(y)
        out_num = 0
        if len(x_b) > len(y_b):
            l_b = x_b[2:]
            s_b = y_b[2:]
        else:
            l_b = y_b[2:]
            s_b = x_b[2:]
        s_b = '0'*(len(l_b)-len(s_b)) + s_b
        for i in range(len(l_b)):
            if l_b[i] != s_b[i]:
                out_num += 1
        return out_num
    
if __name__ == '__main__':
    sl = Solution()
    print(sl.hammingDistance(14,4))