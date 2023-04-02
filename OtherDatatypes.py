#Other Datatypes
#1.Range() - Range is used to generate a sequence of numbers
#Syntax - range(start,stop,step)
print(range(10)) #range(start:0, end:10) end is exclusive
#Convert range object to list
print(list(range(10))) #Stop : start from 0 and stop -1
print(list(range(10,21))) #range(start,stop)
#Fetch even numbers between 10 to 20
print(list(range(10,21,2))) #range(start,stop,step)
#Fetch odd numbers between 10 to 20
print(list(range(11,20,2))) #range(start,stop,step)
#Can we generate negative element in a sequence ? Yes
print(range(-1))
print(list(range(-1,-11,-1))) #if we want -1 to -10
print(list(range(-1,-11,-2))) #range(start,stop,step)

#-------------------------------------------------------------

#Frozen Set - Immutable set
k = [10,20,30,10,20]
print(k)
print(frozenset()) #Empty Frozen Set
print(frozenset(k)) #Supply iterables in it
print(frozenset('amitabh'))
#Difference between Set and Frozenset
#1.Mutability - Set is Mutable,
# Frozen Set is Immutable(once frozenset is created, its elements cannot be changed
#2.Hashability - Set is not hashable because it is mutable and its value changes when its element changes,
# Frozen Set is hashable because it is immutable and can be used as a dictionary key or as an element in another set
#3.Creation - Set is created using curly braces {} or the set(),
#Frozen Set is created by using frozen()
#4.Methods - Set provides methods to add,remove and modify
#Frozen Set only provides methods to access its elements

#--------------------------------------------------------------------------

#Bytes
print(bytes()) #Create Bytes
b = bytes()
print(b)
print(type(b)) #Check its class type
s = bytes([10,20,30])
print(s)
print(s[0]) #indexing (+ve)
print(s[-1]) #indexing (-ve)
print(s[::-1]) #Reversed
#Background Data Structure of Bytes is an Array
#Bytes must be in Range(0,256)
#Bytes is immutable datatypes
#Bytes contains all methods of string

#-------------------------------------------------------------

#Bytearray() - If we want mutable byte sequence
print(bytearray()) #Create Bytearray
s2 = bytearray([100,200,250]) #Must be in Range(0,256)
print(s2)
print(s2[0]) #indexing (+ve)
print(s2[-1]) #indexing (-ve)
#Change 250 to 25
s2[-1] = 25
print(s2[-1])
#Difference between Bytes Vs Bytearray
#Bytes and Bytearray are both used to represent binary data in computer programming
#Byte - a byte is a smallest unit of data in computing and consists of 8bits. Range(0,256)
# - is an immutable sequence of bytes.
# - used to represent fixed length sequence of bytes that will not change.
#Bytearray - is a contiguous block of memory that can store a sequence of byte.
# - is a mutable sequence of bytes.
# - used to represent variable length sequence of bytes that may change.

#-----------------------------------------------------------------------------------------

#None
#its Null in Python - means empty/nothing.

