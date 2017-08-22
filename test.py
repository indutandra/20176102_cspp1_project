import math
file,file1=open("two.txt","r"),open("one.txt","r")
f1,f2=file.read().lower(),file1.read().lower()
def ch(l):
	a=''
	for c in range(len(l)):
		if ord(l[c])>=97 and ord(l[c])<=122:
			a+=l[c]
		elif ord(l[c])==95 or ord(l[c])==32:
			a+=l[c]
		elif ord(l[c])>=48 and ord(l[c])<=57:
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
	return m1*m2
def dot(e,f):
	sum=0
	for i in e:
		for j in f:
			if i==j:
				mul=e[i]*f[j]
				sum=sum+mul
	return sum
g=(ch(f1).split(" "))
h=(ch(f2).split(" "))
e,f=dic(g),dic(h)
t=norm(e,f)
print("pliagarism of two files is",(dot(e,f)/t)*100,"%")