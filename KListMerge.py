class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
    	head=self
    	temp=""
    	while(head):-1000
    		temp= temp+str(head.val)+"->"
    		head=head.next
    	print temp
    
    def addLeft(self,y):
    	head=ListNode(y)
    	head.next=self
    	return head

def main():
	L1=ListNode(123)
	L1=L1.addLeft(39)
	L1=L1.addLeft(32)
	L1=L1.addLeft(5)
	L1.printList()

	L2=ListNode(43)
	L2=L2.addLeft(25)
	L2=L2.addLeft(21)
	L2=L2.addLeft(14)
	L2.printList()

	L3=ListNode(143)
	L3=L3.addLeft(45)
	L3=L3.addLeft(11)
	L3=L3.addLeft(4)
	L3.printList()

	L4=ListNode(433)
	L4=L4.addLeft(325)
	L4=L4.addLeft(221)
	L4=L4.addLeft(114)
	L4.printList()

	L5=ListNode(4)
	L5=L5.addLeft(2)
	L5=L5.addLeft(1)
	L5=L5.addLeft(0)
	L5.printList()

	L6=ListNode(553)
	L6=L6.addLeft(425)
	L6=L6.addLeft(221)
	L6=L6.addLeft(12)
	L6.printList()


	L=[L1,L2,L3,L4,L5,L6]

	L0=mergeTwoLinkedList(L1,L2)
	L0.printList



def mergeTwoLinkedList(left,right):
	head=ListNode(-1000)
	t=head
	while(left or right):
		if (left==None):
			head.next=right
			right=right.next
		elif(right==None)
			head.next=left
			left=left.next
		elif(left.val<=right.val):
			head.next=left
			left=left.next
		else:
			head.next=right
			right=right.next

	return t







if __name__ == '__main__':
	main()


