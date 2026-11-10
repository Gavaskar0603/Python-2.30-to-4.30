'''
print(1)
print(2)
print(3)


for k in range (6):
    print(k)


for j in range(10,0,-1):
    print(j)


a="Livewire"
r=""
for i in a:
   r=i+r
print(r)

#print(10*"Livewire", end="")

for i in range(1,100):
    if i%2==0:
        print(i)


for i in range(3):
    for j in range(3):
        print("0",end = "")
    print()


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()



for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end="")
    print()


for i in range(1):
    print(i)


for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()

a=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{i}x{a}={i*a}")


a=1
while a<=10:
    print(a)
    a+=1    #Assignment


a=10
while a>=0:
    print(a)
    a-=1

#a=10
#while a>=0:
#    print(a)
    

a = 121
t = a
b = 0
while t>0:
    e = t%10        #1%10=1
    b = (b*10)+e    #b = (12*10)+1 = 120+1 = 121
    t = t//10       #1//10 = 0

if a==b:
    print("Palindrome")
else:
    print("Not a palindrome")


a = 124
t = a
s = 0
m = 1
while t>0:
    e = t%10        
    s = s+e
    m = m*e
    t = t//10       

if s==m:
    print("Spy number")
else:
    print("Not a Spy number")
'''
'''
for i in range(1,51):
    if i==11:
        break
    print(i)
        
for i in range(1,51):
    if i==11:
        continue
    print(i)
        


a = 10
b = 0
if b>0:
    print(a/b)
else:
    pass



'''
'''
n = int(input("Enter the value:"))
for i in range(2,n):
    if n%i==0:
        print(n,"is not a prime")
        break
else:
    print(n,"is a prime")
'''
'''
s = "python"

print(s.upper())
print(s.capitalize())
print(s.casefold())
print(s.center(20,"*"))
print(s.count("y"))
print(s.encode())
print(s.endswith("n"))
print(s.expandtabs())
print(s.find("o"))
print(s.format())
print(s.format_map("o"))
print(s.index("h"))
print(s.isalnum())
print(s.isalpha())
print(s.isascii())

print(s.split("t"))
print(s.rsplit("t"))
print(s.strip())
print(s.rstrip())


print(s[3])
print(len(s))


a = ["Bike","Car","Aeroplane","Ship","Boat","Train"]

print(a[::-1])
print(a[:-1])

b =10,20
print(b)
'''
#Core DataType
'''
a=[1,5,8,6,100,3,4,2,7,9,20]
print(type(a))
a.append(100)
print(a)
a.extend([150,200])
print(a)

print(a.count(100))
print(a.index(100))
a.insert(6,1000)
print(a)
a.pop(6)
print(a)
a.remove(100)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
print(a[::-1])
b = a.copy()
print(b)
b.clear()
print(b)
'''
#Tuple
'''
c = (10,20,30,40,10,10)
print(type(c))
print(c.index(20))
print(c[1])
print(c.count(10))
'''
s1 = {11,9,13,3,2,4,6,5}
s2 = {10,8,6,7,3,4,2,1}
print(s1)
print(s2)

s1.add(14)
print(s1)
s1.update({15,12})
print(s1)
print(s1.difference(s2))
print(s1)
#s1.difference_update(s2)
#print(s1)
s1.discard(15)
print(s1)
print(s1.intersection(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
s1.pop()
print(s1)
s1.remove(13)
print(s1)
print(s1.symmetric_difference(s2))
print(s1.union(s2))

d = {"Course":["Java","Python","DA","DS"],
     "Fees":[10000,15000,25000,35000]}
print(d)
import pandas as pd
df = pd.DataFrame(d)
print(df)

print(d.get("Fees"))
print(d.items())
print(d.keys())
#print(d.pop("Fees"))
#print(d)
#print(d.popitem())
d.update({"Duration":[2,3,4,5]})
print(d)
print(d.values())
