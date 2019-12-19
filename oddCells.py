# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:39:29 2019

@author: 11104510

给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。

另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。

你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。

请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。

"""

#import numpy as np

class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        '''
        out_num = 0
        tmp_mat = np.zeros([n,m])
        for i in range(len(indices)):
            tmp_mat[indices[i][0],:] += 1
            tmp_mat[:,indices[i][1]] += 1
            
        tmp_nonzero_array = np.nonzero(tmp_mat)
        for i in range(len(tmp_nonzero_array[0])):
            if tmp_mat[tmp_nonzero_array[0][i],tmp_nonzero_array[1][i]] % 2 != 0:
                out_num += 1
                
        return out_num
        '''
        out_num = 0
        cols = [0] * n
        rows = [0] * m
        for x, y in indices:
            cols[x] += 1
            rows[y] += 1
        for i in range(m):
            for j in range(n):
                if (rows[i]+cols[j]) % 2 != 0:
                    out_num += 1
        return out_num
if __name__ == '__main__':
    sl = Solution()
    print(sl.oddCells(2,2,[[0,1],[1,1]]))