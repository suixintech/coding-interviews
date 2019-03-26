#牛客网剑指offer Python实现
#1、在二維數組中判斷是否存在值target
'''
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
'''
# -*- coding:utf-8 -*-
class Solution1:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array)>=1:
            w,h=len(array),len(array[0])
        i=0
        j=h-1
        while (i<w) &(j>=0):
            print(i,j)
            if array[i][j]>target:
                j-=1
            elif array[i][j]<target:
                i+=1
            else:
                return True
        return False

#2、替換空格
'''
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
# -*- coding:utf-8 -*-
class Solution2:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        su=''
        for word in s:
            if word==' ':
                su+='%20'
            else:
                su+=word
        return su


    
#3、从尾到头打印链表
'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''
#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution3:
# 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is not None:
            return self.printListFromTailToHead(listNode.next)+[listNode.val]
        else:
            return []


