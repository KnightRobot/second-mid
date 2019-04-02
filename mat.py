a=[]
b=[]
c=[]
d=[]
c1=int(input())
r1=int(input())
for i in range(c1):
	for j in range(r1):
		x=int(input())
		b.append(x)
	a.append(b)
	b=[]
print("second")
c2=int(input())
r2=int(input())
for ma in range(c2):
	for na in range(r2):
		l=int(input())
		d.append(l)
	c.append(d)
	d=[]
print(a)
print(c)
result=[]
def size(A):
	return (len(A[0]),len(A))
ra1,c11=size(a)
ra2,c22=size(c)
if True:
	for lo in range(ra1-1):
		for so in range(c22-1):
			for m0 in range(c11-1):
				result[lo][so]+=a[lo][m0]*c[m0][so]
	print(result)
else:
	print("wrong")

