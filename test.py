import math
import os
class bag_of_words(object):
	def ch(self,l):
		a=''
		for c in range(len(l)-1):
			if 48<=ord(l[c])<=57 or 97<=ord(l[c])<=122 or ord(l[c])==95 or ord(l[c])==32:
		 		a+=l[c]
			else:
				c+=1			
		return a
	def dic(self,s):
		d={}
		for c in s:
			if c not in d:
				d[c]=1
			else:
				d[c]+=1
		return d
	def norm(self,e,f):
		sum1,sum2=0,0
		for i in e:
			sum1+=(e[i]**2)
		for j in f:
			sum2+=(f[j]**2)
		m1,m2=math.sqrt(sum1),math.sqrt(sum2)
		return float(m1*m2)
	def dot(self,e,f):
		sum=0
		for i in e:
			for j in f:
				if i==j:
					mul=e[i]*f[j]
					sum=sum+mul
		return sum
p=bag_of_words()
path=input()
l=os.listdir(path)
os.chdir(path)
for i in range(len(l)):
	ll=[]
	for j in range(len(l)):
		if l[i]!=l[j]:
			f1=open(l[i],"r").read().lower()
			k=p.ch(f1).split()
			w=p.dic(k)
			f2=open(l[j],"r").read().lower()
			y=p.ch(f2).split()
			z=p.dic(y)
			nor=p.norm(w,z)
			do=p.dot(w,z)
			ll.append((do/nor)*100)
		else:
			ll.append('null')
	print(ll)