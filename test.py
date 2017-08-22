import math
file,file1=open("one.txt","r"),open("two.txt","r")
f1,f2=file.read(),file1.read()
l1,l2=f1.split(),f2.split()
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
e,f=dic(l1),dic(l2)
t=norm(e,f)
print("pliagarism of two files is",(dot(e,f)/t)*100,"%")



