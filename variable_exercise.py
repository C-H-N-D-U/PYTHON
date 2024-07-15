# This program takes two inputs. The first input stored in a variable called a. The second input stored in a variable called b. WRITE A PROGRAME THAT SWITCHES THE VALUE STORED IN VARIABLES A AND B.

# SOLUTION :

a = input("write number A : ")
b = input("Write number B : ")
c = b
b = a
a = c 
print("A : "+a)
print("B : "+b)