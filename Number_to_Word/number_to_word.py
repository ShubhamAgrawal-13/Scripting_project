
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


t=int(input())
for k in range(0,t):
	n=int(input())
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
	elif(l==13):
		print("One Trillion")
	print()
