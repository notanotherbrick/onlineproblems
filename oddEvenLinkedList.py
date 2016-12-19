# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:54:29 2016

@author: Hobbiton
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


def oddEvenList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        print 'here'
        if not head or notad.next:
            return head
        odd=head
        even=head.next
        
        while head and head.next and head.next.next:
            print head.val
            n1,n2,n3,n4=head,head.next,head.next.next,head.next.next.next
            n1.next=n3
            n2.next=n4
            head=n3
            
        head.next=even
        return odd

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)
n5=ListNode(5)
n6=ListNode(6)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6



def printList(n):
    while n:
        print n.val,
        n=n.next
        
printList(oddEvenList(n1))