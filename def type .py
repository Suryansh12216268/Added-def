'''def add():
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    print("Sum : ", a+b)

add() #function call'''

          #OR

'''def add(x,y): #function call
   print("sum :", a+b)

a = int(input("enter a first number :"))
b = int(input("enter a second number :"))
 add(a,b) #function call'''

'''def calc():
   num1 = int(input("enter first number :"))
   num2 = int(input("enter second number :"))
   mul = num1*num2
   add = num1+num2
   sub = num1-num2
   return(mul,add,sub)

a,b,c = calc()
print("Multiplication answer: ", a,"addition :",b, "subtraction :",c)'''

'''def abc():
    """this a comment inside the function"""
    a = 10


print(abc.__doc__)'''

'''a = 10 # global
def abc():
    a = 20 # local
    print("a = ", a)

print("Value of a outsiude function : ", a)
abc()
print("Value of a outsiude function : ", a)'''

'''def display(nmae,age):
    print("name is=",name,"age is=",age)
display('j',25)
display(40,'s')
display("john",6)
display(age=34,name="abc") #keyword argument'''

'''def display(a,b=10,c=20):
    print("a=",a,"b=",b,"c=",c)

display(15)'''

'''def add(a,b,c=10):
    print("a= ",a,"b = ",b,"c = ",c)

add(10,10)'''

'''a=100
def demo():
    a=10
    print(a)
demo()
print(a)'''

'''a=20
def d():
    global a
    a=30
      print("value of a in fn",a)

d()
print("value of a in outside fn",a)'''
