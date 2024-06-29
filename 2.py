# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 00:03:30 2024

@author: THINK-JZ
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out     = ListNode()
        sum1    = l1.val + l2.val +carry
        out.val = sum1 % 10
        carry_  = sum1 //10
        
        if not l1.next and not l2.next: 
            if carry_:
                out.next= ListNode()
                out.next.val = 1
            return out
        elif not l1.next:
            l1.next = ListNode()
        elif not l2.next: 
            l2.next = ListNode()
        out.next=self.addTwoNumbers(l1.next, l2.next, carry_)
        return out
        
        # print(out.val)