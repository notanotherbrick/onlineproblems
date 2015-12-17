class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def push(self,data):
    	temp=ListNode(data)
    	temp.next=self
    	self=temp
    	self.printlist()

    def printlist(self):
    	a=self
    	temp=""
    	while(a):
    		temp= a.val + "->" 
    		a=a.next
    	print temp



def main():
	head=ListNode("a")
	head.push("b")
	head.push("c")
	head.printlist()




if __name__=="__main__":
	main()