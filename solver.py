# Saurabh Khoria 
# 2013CSB1029
# Lab Test 2


import rubik as r    	# import the contents of the file rubik.py

# Implementing the queue data structure. 

class queue:
	def __init__(self):
		"""
		This method is the default constructor of queue which
		creates an empty list l.
		"""
		self.l=[]

	def enqueue(self,k):
		"""
		This method of queue class enqueues the element
		into the queue.
		"""
		self.l.append(k)

	def dequeue(self):
		"""
		This method of queue class dequeues an element
		from the queue.
		"""
		x=self.l[0]
		del(self.l[0])
		return x

# Defining the class state

class state:
	"""
	This class defines state which has
	3 atributes tuple, parent and child.
	"""
	def __init__(self,s):
		self.tuple=s
		self.parent=None
		self.child=None

# Imolementing the hashtable

class hashtable:
	"""
	This class is the implementation of the 
	hashtable
	"""
	def __init__(self):
		"""
		This method is the defualt constructor
		of the class hashtable which creates an 
		empty hashtable of size 100000
		"""
		self.l=[]
		for i in range(100000):
			self.l.append([])

	def insert(self,s):
		"""
		This method hashes the state s
		into the hashtable.

		"""
		d=hashf(s.tuple)
		self.l[d].append(s)

	def search(self,s):
		"""
		This method checks whether the hashtable 
		has the state s in it or not.
		"""
		d=hashf(s)
		for i in range(len(self.l[d])):
			if s==self.l[d][i].tuple:
				return 1

def hashf(t):
	"""
	This function returns the key corresponding to which the tuple t will
	be hashed in the hashtable.
	"""
	d=0
	for i in range(24):
		d*=10
		d+=t[i]
	return d%99991


def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    
    """

    if start==end:
    	return []

    p=queue()
    q=queue()

    hash1=hashtable()
    hash2=hashtable()

    s=state(start)
    hash2.insert(s)
    p.enqueue(s)
    p.enqueue(None)

    s=state(end)
    hash1.insert(s)
    q.enqueue(s)
    q.enqueue(None)

    def returnmid():
		level=1
		while(1):
			if level>7:
				return  None

			a=q.dequeue()
			while(a!=None):
				for i in range(6):
					b=r.perm_apply(r.quarter_twists[i],a.tuple)
					k=0
					if hash1.search(b):
						k=1
					if k==0:
						s=state(b)
						s.parent=a
						q.enqueue(s)
						hash1.insert(s)
						for i in range(len(hash2.l[hashf(b)])):
							if b==hash2.l[hashf(b)][i].tuple:
								hash2.l[hashf(b)][i].parent=a
								return hash2.l[hashf(b)][i]
				a=q.dequeue()

			q.enqueue(None)


			c=p.dequeue()
			while(c!=None):
				for i in range(6):
					d=r.perm_apply(r.quarter_twists[i],c.tuple)
					k=0
					if hash2.search(d):
						k=1
					if k==0:
						s=state(d)
						s.child=c
						p.enqueue(s)
						hash2.insert(s)
						for i in range(len(hash1.l[hashf(d)])):
							if d==hash1.l[hashf(d)][i].tuple:
								hash1.l[hashf(d)][i].child=c
								return hash1.l[hashf(d)][i]
				c=p.dequeue()

			p.enqueue(None)

			level+=1

	
    mid=returnmid()
    x=mid
    y=mid

    if mid==None:
    	return None

    u=[]
    while x.tuple!=start:
    	for i in range(6):
    		b=r.perm_apply(r.quarter_twists[i],x.tuple)
    		if b==x.child.tuple:
    			if i%2==0:
    				u.append(r.quarter_twists[i+1])
    			else:
    				u.append(r.quarter_twists[i-1])
    			break
    	x=x.child

    path1=u[::-1]

    v=[]
    while y.tuple!=end:
    	for i in range(6):
    		b=r.perm_apply(r.quarter_twists[i],y.tuple)
    		if b==y.parent.tuple:
    			v.append(r.quarter_twists[i])
    			break
    	y=y.parent

    path2=v

    path=path1+path2

    return path
