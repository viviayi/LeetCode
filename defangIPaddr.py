# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:46:27 2019

@author: 11104510

给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。

所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(r'.',r'[.]')
    
if __name__ == '__main__':
    sl = Solution()
    print(sl.defangIPaddr('0000.0000.0000.0000'))