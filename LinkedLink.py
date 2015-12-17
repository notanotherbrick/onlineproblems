class node:
	def __init__(self,data):
		self.data= data
		self.next= None

class linkedlist:
	def __init__(self):
		self.head=None

	def push(self,new_data):
		new_node=node(new_data)
		new_node.next=self.head
		self.head = new_node

	def insertAfter(self, prev_node,new_data):
		if prev_node== None:
			print "node must be in linkedlist"
			return

		new_node=node(new_data)
		new_node.next=prev_node.next
		prev_node.next=new_node

	def append(self,new_data):
		new_node=node(new_data)

		if self.head is None:
			self.head=new_node
			return

		last=self.head
		while(last.next):
			last=last.next

		last.next=new_node

	#		new_head.next=prev_node
	def middlenode(self,head):
		try:
			slow=head
			fast=head
			while(fast):
				fast=fast.next.next
				slow=slow.next

			return slow
		except:
			return slow

	def merge2listreverseorder(self,other):
		a=self.head
		b=other.head
		c=None

		while(a or b):
			
			if (a == None):
				temp=b.next
				b.next=c
				c=b
				b=temp
			elif (b == None):
				temp=a.next
				a.next=c
				c=a
				a=temp

			else:
				if(a.data >= b.data ):
					if c==None:
						temp=b.next
						c=b
						c.next=None
						b=temp
					else:
						temp=b.next
						b.next=c
						c=b
						b=temp


				else:
					if c==None:
						temp=a.next
						c=a
						c.next=None
						a=temp
					else:
						temp=a.next
						a.next=c
						c=a
						a=temp
		printlist(c)

	def stringcompare(self,other):
		a=self.head
		b=other.head

		while(a or b):
			if a == None:
				return -1

			elif b == None:
				return 1
			elif (a.data < b.data):
				return -1
			elif (a.data > b.data):
				return 1
			a=a.next
			b=b.next


		return 0

	def reverselist(self,head):
		if head == None:
			return 


		prev=None
		curr=head
		while(curr): 
			next_node=curr.next
			curr.next=prev
			prev=curr
			curr=next_node

		return prev


	def isPalindrone(self):
		mid=self.middlenode(self.head)
		end=self.reverselist(mid)


		begin=self.head
		print getLength(begin)
		print getLength(end)
		while(begin != None and end != None):
			print "begin data", begin.data
			print "end data", end.data
			if (begin.data!=end.data):
				print "herhehwehhwreh"
				return False
				break
			begin=begin.next
			end=end.next

			return True

	def getLength(self):
		i=0
		t=self.head
		while(t):
			i=i+1
			t=t.next

		return i


def recurrRevList(head):
	if head.next==None:
		return head

	temp=head.next
	head.next=None
	t=recurrRevList(temp)
	temp.next=head
	return t


def main():
	ll1=linkedlist()
	ll1.append(1)
	ll1.append(1)
	ll1.append(0)
	ll1.append(1)
	# ll1.append(30)
	# ll1.append(1)
	# ll1.append(3)
	# ll1.append(4)
	printlist(ll1.head)
	print ll1.middlenode(ll1.head).data
	print ll1.isPalindrone()

	#t=recurrRevList(ll1.head)
	#printlist(t)
	print "List has ",ll1.getLength(), " elements"


def main2():

	# ll2=linkedlist()
	# ll2.append('c')
	# ll2.append('d')
	# ll2.append('e')
	# printlist(ll2.head)

	#ll2.merge2listreverseorder(ll1)
	#print ll1.stringcompare(ll2)
# why does (ll1.middlenode).data does not work
	ll1.middlenode(ll1.head)

	# ll1=linkedlist()
	#print ll1.isPalindrone()
	#printlist(ll1.reverselist(ll1.head))
	tree1=TreeNode(1)
	tree2=TreeNode(2)
	tree3=TreeNode(3)
	tree4=TreeNode(4)
	tree5=TreeNode(5)
	tree6=TreeNode(6)
	tree1.left=tree2
	tree1.right=tree5
	tree2.left=tree3
	tree2.right=tree4
	tree5.right=tree6

	ll3=linkedlist()
	h=flattentree(tree1,ll3)
	printlist(h.head)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def flattentree(root,head):
	if root.right != None:
		flattentree(root.right,head)
	if root.left != None:
		flattentree(root.left,head)
	head.push(root.val)
	return head

def printlist(temp):
		listcontent=""
		while(temp):
			listcontent= listcontent + str(temp.data)+ " -> "
			temp=temp.next

		print listcontent

if __name__=='__main__':
	main()




# for a circular linked list ; find joined node
# two lists merge into one, find point of merging