import math
import os
def ch(l):
	a=''
	for c in range(len(l)-1):
		if c==0:
			a+=l[c]
		elif c==l[len(l)-1]:
			a+=l[c]
		else:
			if ord(l[c+1])==32 or ord(l[c-1])==32:
				if 97<=ord(l[c])<=122 or 48<=ord(l[c])<=57 or ord(l[c])==95 or ord(l[c])==32:
			 		a+=l[c]
				else:
					a+=" "
					c+=1
			else:
				if 48<=ord(l[c])<=57 or 97<=ord(l[c])<=122 or ord(l[c])==95 or ord(l[c])==32:
			 		a+=l[c]
				else:
					c+=1			
	return a
def dic(s):
	d={}
	for c in s:
		if c not in d:
			d[c]=1
		else:
			d[c]+=1
	return d
def norm(e,f):
	sum1,sum2=0,0
	for i in e:
		sum1+=(e[i]**2)
	for j in f:
		sum2+=(f[j]**2)
	m1,m2=math.sqrt(sum1),math.sqrt(sum2)
	return float(m1*m2)
def dot(e,f):
	sum=0
	for i in e:
		for j in f:
			if i==j:
				mul=e[i]*f[j]
				sum=sum+mul
	return sum
path=input()
l=os.listdir(path)
os.chdir(path)
for i in range(len(l)):
	ll=[]
	for j in range(len(l)):
		if l[i]!=l[j]:
			f1=open(l[i],"r").read().lower()
			k=ch(f1).split()
			w=dic(k)
			f2=open(l[j],"r").read().lower()
			y=ch(f2).split()
			z=dic(y)
			nor=norm(w,z)
			do=dot(w,z)
			ll.append((do/nor)*100)
		else:
			ll.append('null')
	print(ll)