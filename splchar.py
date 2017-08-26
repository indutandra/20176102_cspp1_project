n = int(input().strip())
l=[]
while(n > 0):
    remainder = n%2
    n = n//2
    l.append(remainder)
print(l)
s=0
c=[]
for i in l:
	if i==1:
		s=s+1
		c.append(s)
	else:
		c.append(s)
		s=0

print(max(c))

