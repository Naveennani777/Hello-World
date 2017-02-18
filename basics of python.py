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
