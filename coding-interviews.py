#!/usr/bin/python3
#-*-coding:utf-8 -*-
# __Author__  : 随心
# __Time__    : 2019/3/26 10:26 PM
# __File__    : coding-interviews.py
# __Software__: PyCharm

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


#4、重构二叉树
'''
输入某二叉树的前序遍历和中序遍历的结果，
请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和
中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
{1,2,5,3,4,6,7}
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution4_1:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write co de here
        if len(pre)==0 or len(tin)==0:
            return None
        root_data=TreeNode(pre.pop(0))
        k=tin.index(root_data.val)
        root_data.left=self.reConstructBinaryTree(pre,tin[:k])
        root_data.right=self.reConstructBinaryTree(pre,tin[k+1:])
        return root_data

class Solution4_2:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(tin) == 0:
            return None
        else:
            root = TreeNode(pre[0])
            slt = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:1+slt],tin[:slt])
            root.right = self.reConstructBinaryTree(pre[1+slt:],tin[slt+1:])
        return root


#5、用两个栈实现队列
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 
队列中的元素为int类型。
'''
# -*- coding:utf-8 -*-
class Solution5:
    def __init__(self):
        self.stack1=[1,2,3]  #入栈
        self.stack2=[5,6,7]  #出栈

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                return self.stack2.pop()

#6、旋转数组中的最小数字
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，
该数组的最小值为1。 
NOTE：给出的所有元素都大于0，
若数组大小为0，请返回0。
'''
# -*- coding:utf-8 -*-
class Solution6:
    def minNumberInRotateArray1(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        else:
            minvalue=min(rotateArray)
            return minvalue
    def minNumberInRotateArray2(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        else:
            temp=2^32
            for vale in rotateArray:
                if temp>vale:
                    temp=vale
            return temp

#7、斐波那契数列
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
1、1、2、3、5、8、13、21、34
'''
# -*- coding:utf-8 -*-
class Solution7:
    def Fibonacci1(self, n):
        # write code here
        result=[0,1]
        if n<2:
            return result[n]
        else:
            return self.Fibonacci1(n-1)+self.Fibonacci1(n-2)

    def Fibonacci2(self,n):
        n1=1
        n2=1
        result=0
        if n==0:
            return 0
        elif n<=2:
            return 1
        else:
            for i in range(3,n+1):
                result=n1+n2
                n1=n2
                n2=result
            return result

#8、跳台阶
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

# -*- coding:utf-8 -*-
class Solution8:
    def jumpFloor(self, number):
        # write code here
        if number==0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        else:
            n1=1
            n2=1
            n3=0
            for i in range(3,number+2):
                n3=n1+n2
                n1=n2
                n2=n3
            return n3

    def jumpFloor1(self,number):
        result=[0,1,2]
        if number<=2:
            return result[number]
        else:
            return self.jumpFloor1(number-1)+self.jumpFloor1(number-2)





#9、变态跳台阶
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
# -*- coding:utf-8 -*-
class Solution9:
    def jumpFloorII(self, number):
        # write code here
        if number==0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        elif number==3:
            return 4
        else:
            n2=4
            n3=0
            for i in range(4,number+1):
                n3=n2*2
                n2=n3
            return n3
    def jumpFloorII1(self,number):
        result=[0,1,2,4]
        if number<=3:
            return result[number]
        else:
            return self.jumpFloorII1(number-1)*2




#10、矩阵覆盖
'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法
'''
# -*- coding:utf-8 -*-
class Solution10:
    def rectCover(self, number):
        # write code here
        if number==0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        else:
            n1=1
            n2=2
            n3=0
            for i in range(3,number+1):
                n3=n1+n2
                n1=n2
                n2=n3
            return n3

    def rectCover1(self,number):
        result=[0,1,2]
        if number<=2:
            return result[number]
        else:
            return self.rectCover1(number-1)+self.rectCover1(number-2)


#11、二进制中1的个数
'''
输入一个整数，输出该数二进制表示中1的个数。
其中负数用补码表示。
'''
# -*- coding:utf-8 -*-
class Solution11:
    result = []
    def NumberOf1(self, n):
        # write code here
        if n==0:
            return 0
        for i in range(33):
            if n==2**i:
                self.result.append(i)
                n=0
                break
            elif n<(2**i):
                n=n-2**(i-1)
                self.result.append(i)
                break
        if n>0:
            self.NumberOf1(n)
            return len(self.result)
        elif n==0:
            return len(self.result)

    def NumberOf2(self,n):
        s=0
        if n<0:
            n = n & 0xffffffff
        while (n!=0):
            s+=1
            n=n&(n-1)
        return s


#12、数值的整数次方
'''
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
'''
# -*- coding:utf-8 -*-
class Solution12:
    def Power(self, base, exponent):
        # write code here
        if exponent==0:
            return 1
        elif exponent>0:
            return eval('*'.join([str(base)]*exponent))
        elif exponent<0:
            return 1/eval('*'.join([str(base)] * abs(exponent)))

        
