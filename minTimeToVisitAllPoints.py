# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:55:52 2019

@author: 11104510

平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的最小时间（以秒为单位）。

你可以按照下面的规则在平面上移动：

每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
必须按照数组中出现的顺序来访问这些点。

"""

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        for i in range(len(points)-1):
            time += max(abs(points[i][0]-points[i+1][0]),abs(points[i+1][1]-points[i][1]))
        return time

if __name__ == '__main__':
    sl = Solution()
    print(sl.minTimeToVisitAllPoints([[0,0],[1,1]]))