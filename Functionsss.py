def demo(name, course):
    print(f"Hello {name}, this is {course} class")
demo("Hari","Java")


def demo1(name, course):
    print(f"Hello {name}, this is {course} class")
demo1(course="Java",name="Surya")


def demo2(name = "Surya",course="python"):
    print(f"Hello {name}, this is {course} class")
demo2()
demo2("Kumar","DS")


def demo3(*number):
    total = 1
    for i in number:
        total*= i
    print(total)
demo3(11,12,13,14,5,16,17,18)


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
print(fact(6))


add = lambda a,b : a*b
print(add(10,2))


l = [1,2,3,4,5,6,7,8,9,10]
odd = list(filter(lambda x : x%2!=0,l))
print(odd)


def demo4():
    print("Helloo...")
    return
    print(1000)
print(demo4())

def local():
    a=10
    b=20
    print(a+b)
local()
#print(a)

c=100
d=500
def global1():
    print(c+d)
global1()
print(d)
