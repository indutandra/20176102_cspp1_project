import os
def ch(l):
	a=''
	for c in range(len(l)):
		if 48<=ord(l[c])<=57 or 97<=ord(l[c])<=122 or ord(l[c])==95 or ord(l[c])==32:
			a+=l[c]
		else:
			c+=1	
	return a
def lcs(l,l1):
	lcs=0
	for i in range(len(l)):
		for j in range(len(l1)):
			a=[]
			while i<len(l) and j<len(l1) and l[i]==l1[j]:
				a.append(l[i])
				i+=1
				j+=1
			b=' '.join(a)
			b=b.strip()
			if len(b)>lcs:
				lcs=len(b)
	lcs1=((lcs*2)/((len(f1)+len(f2))))*100
	return lcs1
path=input()
c=os.listdir(path)
os.chdir(path)
for i in range(len(c)):
	l2=[]
	for j in range(len(c)):
		if i!=j:
			f1=open(c[i],"r").read().lower()
			k=(ch(f1)).split()
			f2=open(c[j],"r").read().lower()
			w=ch(f2).split()
			lcs2=lcs(k,w)
			l2.append(lcs2)
		else:
			l2.append("null")
	print(l2)