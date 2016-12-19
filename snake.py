


class Snake(object):
	def __init__(self,width,length):
		if width<3 or length <3:
			print 'Arena too small'
		self.arena = [[[-1,-1]for _ in xrange(width)] for _ in xrange(length)]
		self.direction = 'r' # self.direction takes values right, left, top, bottom
		
		self.head = [width/2,length/2]
		self.tail = [width/2 - 1, length/2]


		# set pointer to next node 
		arena[self.tail[0]][[self.tail[1]] = [self.head[0], [self.head[1]] 

		self.food = [width-1,length/2]

	def get_next(self):
		while 1:
			# get user input
			curr_dir=get_user_input()

			# if no user_input, continue in last direction
			if not curr_dir:
				curr_dir=self.direction
			# else update the snake direction
			else:
				self.direction=curr_dir

			


			next



	def get_user_input(self):
		# returns 'l','r','b','t' coressponding to right, left, top, bottom or None
