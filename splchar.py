def ch(l):
	a=''
	for c in range(len(l)):
		if c==0:
			a+=l[c]
		elif c==l[len(l)-1]:
			a+=l[c]
		else:
			if ord(l[c+1])==32 or ord(l[c-1])==32:
				if ord(l[c])>=97 and ord(l[c])<=122:
			 		a+=l[c]
				elif (ord(l[c])==95 or ord(l[c])==32):
					a+=l[c]
				elif (ord(l[c])>=48 and ord(l[c])<=57):
					a+=l[c]
				else:
					a+=" "
					c+=1			
			else:
				if ord(l[c])>=97 and ord(l[c])<=122:
			 		a+=l[c]
				elif (ord(l[c])==95 or ord(l[c])==32):
					a+=l[c]
				elif (ord(l[c])>=48 and ord(l[c])<=57):
					a+=l[c]
				else:
					c+=1