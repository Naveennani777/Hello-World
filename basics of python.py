print ("Program with comparison operator , if statement, for loop and dynamically passing values")
print ("Enter n value greaterthan 10 and d value lessthan 20")
n = int(input("enter a number for n value: "))
d = int(input("enter a number for d value: "))
a = input("Enter a name: ") 
if n > 10 and d < 20:
  print ("entered values are equal with n and d " , n ,d)
  print ("values given for n and d are 10 and 20")
else:
  print ("Entered values are not equal")

if a == "march":
    print ("Entered month is correct")
else:
    print ("Entered month is not correct")
  
  
num = int(input("Enter a value: "))
print (num)
num1 = (str(num))
print ( " num1 is:" , num1[0])
first_value = num1[0]
print ("num1 or first_value is" , first_value)
value1 = "00"
print ("value1 is: " ,value1)
value2 = ( str(value1))
print (" after converting value1 to string and value2 is : " ,value2)
value3 = (first_value+value2)
print (value3)
value4 = (int(value3))
print (value4)
final_value = ( num - value4 )
print ("Number selcted by you is: " , final_value)


Number = int(input("Enter a number to see table program: "))
for i in range(1, 11):
    answer = Number * i
    print ( Number , "*" , i , "= " , answer)
    
a = 1
while a<11:
  print (a)
  a += 1
print ("\n")
for x in range(1, 11):
  print (x)
  x += 1
  
print ("Programs with while loop and for loop")  
a = 1
s = 1
print ("Enter 0 to quit! \n")
while a != 0:
  print ("Current sum " , s)
  a = int(input("Enter Number: "))
  s += a
  
  
print ("Programs with list comparison and dict comparison")  
a=b=6633
a='6633' #It is true between integers and strings
b='6633'
#a=[1,2,3,4] # here logically it is false between two lists.
#b=[1,2,3,4]
#a,b,c,d = 10,20,30,10
if a is b:
  print ("true")
else:
  print ("False")

dict1 = {'one':'4','two':'6'}
dict2 = {'one':'1','two':'2'}
if dict1 != dict2:
  print ("dict1 and dict2 are equal")
else:
  print ("two dicts are not equal")
  
print ("slicing feature \n")
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,14,15,16,17,18,19,20]
print (list1[:]) #prints whole list
print (list1[0:5]) #prints 1,2,3,4,5
dict1 = {'one':'1','two':'2','three':'3'}
print (dict1)
print (dict1.keys())
print (dict1.values())
print (list1.append(11))
print (list1)
list1.extend(list2)
print (list1)
dict2 = {'four':'1,2,3,4','five':'5','six':'6'}
print (dict2)
dict3 = {'seven,eight,nine,ten':'7','eleven':'11'}
print (dict3.values())    


print ("Basics of python and conditional statements")
a = int(input("Enter a number: "))
#a = 20
if a>0:
  print (a ," is greater than zero ")
else:
  print (a,"is less than zero")
  
sum=20+30
print (sum)

a = int(input("Enter number: a  "))
b = int(input("Enter number: b"))
c = int(input("Enter number: c "))

#a = -10
#b = -20
#c = -30

print ("maximum of a,b,c :" ,a,b,c,  "are: "  ,max(a,b,c))

name = input("name:?")
if name == "jan":
  print (" Entered name is " , name)
elif name =="feb":
  print (" Entered name is " , name)
elif name == "mar":
  print (" Entered name is " , name)
elif name == "april":
  print (" Entered name is " , name)
else:
  print ("Entered name is not in list" , name)

  
print ("Defining classes")
a = 2
print(id(a))
print(type(a))
print(a)
b = 3
print(id(b))
print(type(b))
print(b)
c = 3.4
print(type(c))
d =[]
e={}
f=()
print(type(d))
print(type(e))
print(type(f))
g =2 
print(id(g))
x=y=[1,2]
z={1,2}
print(id(x))
print(id(y))
print(type(z))
abc=""
print(type(abc))

print("output of programs")
140302468389984
<class 'int'>
2
140302468390016
<class 'int'>
3
<class 'float'>
<class 'list'>
<class 'dict'>
<class 'tuple'>
140302468389984
140302410408008
140302410408008
<class 'set'>
<class 'str'>

**************
print("\n**************\n")
print ("Defining a class")

class Naveen:
  def Nani(self):
    print ("Welcome to classes")
    print ("Welcome to python")
a=Naveen()
a.Nani()

print("\n**************\n")
class Mahesh:
  def __init__(self):
   self.name="I am eldest"
   self.var="Family club"
  def Nani1(self,name2):
    print ("I am eldest " , name2)
    self.Nani2(22,23,24,5,23,234,243)
  def Nani2(self,*args):
    for arg in args:
      print ("One is eldest" , arg)
    print("I am youngest")
    
    
b=Mahesh()
print (b.name)
print(b.var)
b.Nani1("Sachin")
b.Nani2("Naveennani","Manojnani")

print("\n**************\n")

print ("output of above defined classes")
Defining a class
Welcome to classes
Welcome to python

**************

I am eldest
Family club
I am eldest  Sachin
One is eldest 22
One is eldest 23
One is eldest 24
One is eldest 5
One is eldest 23
One is eldest 234
One is eldest 243
I am youngest
One is eldest Naveennani
One is eldest Manojnani
I am youngest

**************
print("\n**************\n")

print ("\nDefine a class\nInitialize variables in class using Constructor\nGet values of one function into another function within sameclass\nCreate an object for the class defined\nCall the functions in class using object\nPrint output\n")

class Fruits():
  def __init__(self):
    self.fruit1 = "apple"
    self.fruit2 = "banana"
    self.a = 10
  def Vegetable(self):
    self.veg1 = "bottleguard"
    self.veg2 = "bitterguard"
    print (self.veg1)
    print (self.veg2)
  def Car(self,*args):
    for arg in args:
      print ("Indian cars are" , arg)
  def Health(self,value):
    if (value == "bitterguard"):
      self.a += 10
      print("bitterguard makes health strong" , self.a)
    elif (value == "liquor"):
      self.a -= 10
      print("liquor makes health weak" , self.a)
      
x=Fruits()
print(x.fruit1)
print(x.fruit2)
print(x.a)
x.Health("bitterguard")
x.Health("liquor")
x.Vegetable()
x.Car("maruthi","TATA","Mahendra")      

print("output of above written classes and functions")
Define a class
Initialize variables in class using Constructor
Get values of one function into another function within sameclass
Create an object for the class defined
Call the functions in class using object
Print output

apple
banana
10
bitterguard makes health strong 20
liquor makes health weak 10
bottleguard
bitterguard
Indian cars are maruthi
Indian cars are TATA
Indian cars are Mahendra
