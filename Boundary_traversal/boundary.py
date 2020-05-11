#!/bin/usr/python

class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


def insert(root,data,q):
	node=Node(data)
	if(root==None):
		root=node
	elif(q[0].left==None):
		q[0].left=node
	else:
		q[0].right=node
		q.pop(0)
	q.append(node)
	return root

def removeMinusOne(root):
	if(root==None):
		return root

	if(root.data==-1):
		return None
	if(root.left!=None):
		root.left = removeMinusOne(root.left)
	if(root.right!=None):
		root.right = removeMinusOne(root.right)
	return root

def leafnodes(root,sum2):
	if(root==None):
		return
	if(root.left==None and root.right==None):
		sum2.append(root.data)
		return
	leafnodes(root.left,sum2)
	leafnodes(root.right,sum2) 


def leftboundary(root,sum1):
	if(root==None):
		return 
	if(root.left==None and root.right==None):
		return 
	if(root.left!=None):
		sum1.append(root.data)
		leftboundary(root.left,sum1)
	elif(root.right!=None):
		sum1.append(root.data)
		leftboundary(root.right,sum1)

def rightboundary(root,sum3):
	if(root==None):
		return 
	if(root.left==None and root.right==None):
		return 
	if(root.right!=None):
		sum3.append(root.data)
		rightboundary(root.right,sum3)
	elif(root.left!=None):
		sum3.append(root.data)
		rightboundary(root.left,sum3)

def totalSum(root,order):
	total=0
	if(root==None):
		return total
	#total+=root.data
	sum1=[0]
	#leftboundary(root.left,sum1)
	leftboundary(root,sum1)
	# print(sum1)
	order.extend(sum1[1:len(sum1)])
	sum2=[0]
	leafnodes(root,sum2)
	# print(sum2)
	order.extend(sum2[1:len(sum2)])
	sum3=[0]
	#rightboundary(root.right,sum3)
	rightboundary(root,sum3)
	# print(sum3)
	rev=sum3[1:len(sum3)]
	rev.reverse()
	order.extend(rev)
	
	for i in sum1:
		total+=i
	for i in sum2:
		total+=i
	for i in sum3:
		total+=i

	return total



def inorder(root):
	if(root==None):
		return 
	inorder(root.left)
	print(root.data," ")
	inorder(root.right)

def printTree(root,sp):
	if(root==None):
		return
	printTree(root.right,sp+5)
	print(" "*sp,root.data)
	printTree(root.left,sp+5)



def mprint(n):
	if(n==1000000):
		print("One Million",end=" ")
	else:
		t1=n%1000000
		t2=(n-t1)//1000000
		threeprint(t2)
		if(t2!=0):
			print("Million",end=" ")
		if(t1!=0):
			tprint(t1)




def tprint(n):
	if(n==1000):
		print("One Thousand",end=" ")
	else:
		t1=n%1000
		t2=(n-t1)//1000
		threeprint(t2)
		if(t2!=0):
			print("Thousand",end=" ")
		if(t1!=0):
			threeprint(t1)


def threeprint(n):
	if(n==100):
		print("One Hundred",end=" ")
	else:
		t1=n%100
		t2=(n-t1)//100
		if(t2!=0):
			print(toword(t2),"Hundred",end=" ")
		if(t1!=0):
			twoprint(t1)




def twoprint(n):
	if(n<=20):
		print(toword(n),end=" ")
	elif(n<100):
		t1=n%10
		t2=n-t1
		if(t2!=0):
			print(toword(t2),end=" ")
		if(t1!=0):
			print(toword(t1),end=" ")


def toword(n):
    if(n==0):
        return "Zero"
    if(n==1):
        return "One"
    if(n==2):
        return "Two"
    if(n==3):
        return "Three"
    if(n==4):
        return "Four"
    if(n==5):
        return "Five"
    if(n==6):
        return "Six"
    if(n==7):
        return "Seven"
    if(n==8):
        return "Eight"
    if(n==9):
        return "Nine"
    if(n==10):
        return "Ten"
    if(n==11):
        return "Eleven"
    if(n==12):
        return "Twelve"
    if(n==13):
        return "Thirteen"
    if(n==14):
        return "Fourteen"
    if(n==15):
        return "Fifteen"
    if(n==16):
        return "Sixteen"
    if(n==17):
        return "Seventeen"
    if(n==18):
        return "Eighteen"
    if(n==19):
        return "Nineteen"
    if(n==20):
        return "Twenty"
    if(n==30):
        return "Thirty"
    if(n==40):
        return "Forty"
    if(n==50):
        return "Fifty"
    if(n==60):
        return "Sixty"
    if(n==70):
        return "Seventy"
    if(n==80):
        return "Eighty"
    if(n==90):
        return "Ninety"
    if(n==100):
        return "Hundred"
    if(n==1000):
        return "Thousand"
    return None	


def number_to_word(n):
	l=len(str(n))
	if(l<3):
		twoprint(n)
	elif(l<4):
		threeprint(n)
	elif(l<7):
		tprint(n)
	elif(l<10):
		mprint(n)
	elif(l<13):
		if(n==1000000000):
			print("One Billion")
		else:
			t1=n%1000000000
			t2=(n-t1)//1000000000
			threeprint(t2)
			if(t2!=0):
				print("Billion",end=" ")
			if(t1!=0):
				mprint(t1)
	elif(l==3):
		print("One Trillion")
	# print()





list_of_nodes= [int(x) for x in input().split()]

# for i in list_of_nodes:
# 	print(2*i)

n=len(list_of_nodes)
j=0
i=0
root=None
q=[]

while(i<n):
	root=insert(root,list_of_nodes[i],q)
	i+=1
	
# inorder(root)
# printTree(root,0)

root=removeMinusOne(root)
# print("hello")
# inorder(root)
print("Tree: ")
printTree(root,0)

# sum1=[]
# leftboundary(root,sum1)
# print(sum1)

# sum2=[]
# leafnodes(root,sum2)
# print(sum2)

# sum3=[]
# rightboundary(root,sum3)
# print(sum3)
order=[]
total=totalSum(root,order)
# print(total)
number_to_word(total)
print()

print("Order = [ ",end="")
for i in range(0,len(order)-1):
	number_to_word(order[i])
	print(", ",end="")
number_to_word(order[len(order)-1])
print("]")


