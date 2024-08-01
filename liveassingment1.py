#write a code to revrse a string

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "pwforskills"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))

# Q.2 write a code to count the numbers of vowels in a string

string = "himanshu!"
vowels = "aeiouAEIOU"
 
count = sum(string.count(vowel) for vowel in vowels)
print(count)


#Q.3 write a code to check if a given string is a palindrome or not

# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

    #Q.4 write a code to check if two given string are anagrams of each other

# Function to check if two strings are anagrams
def are_anagrams(s1, s2):
    # Sort both strings and compare
    return sorted(s1) == sorted(s2)


# Test cases
if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"

    if are_anagrams(str1, str2):
        print("True")
    else:
        print("False")

    str1 = "gram"
    str2 = "arm"

    if are_anagrams(str1, str2):
        print("True")
    else:
        print("False")

#Q.5write a code to find all occurence of a given substring within another string

test_str = "pwforskils is best for skills"
  
test_sub = "skills"
  
print("The original string is : " + test_str) 
  
# printing substring 
print("The substring to find : " + test_sub) 
  
# using list comprehension + startswith() 
# All occurrences of substring in string 
res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 
  
# printing result 
print("The start indices of the substrings are : " + str(res)) 

#Q.6 write a code to perfom basic string comperssion using the counts of repeated charcter












#Q,7 write a code to determine if a string has all unique charcter

def uniqueCharacters(str):
     
    # If at any time we encounter 2 
    # same characters, return false
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if(str[i] == str[j]):
                return False;
 
    # If no duplicate characters 
    # encountered, return true
    return True;
 
 
# Driver Code
str = "pwforskills";
 
if(uniqueCharacters(str)):
    print("The String ", str," has all unique characters");
else:
    print("The String ", str, " has duplicate characters");
 
#Q.8 write a code to convert a given string to upper case or lower case


def convertOpposite(str):
    ln = len(str)
 
    # Conversion according to ASCII values
    for i in range(ln):
        if str[i] >= 'a' and str[i] <= 'z':
 
            # Convert lowercase to uppercase
            str[i] = chr(ord(str[i]) - 32)
 
        elif str[i] >= 'A' and str[i] <= 'Z':
 
            # Convert lowercase to uppercase
            str[i] = chr(ord(str[i]) + 32)
 
# Driver code
if __name__ == "__main__":
    str = "PwFoRsKIlS"
    str = list(str)
 
    # Calling the Function
    convertOpposite(str)
 
    str = ''.join(str)
    print(str)

    #Q.9 write a code to count the numbers of words in string

    # Python program to count total
# number of words in the string


def countWords(s):

    # Check if the string is null
    # or empty then return zero
    if s.strip() == "":
        return 0

    # Splitting the string

    words = s.split()

    return len(words)


if __name__ == "__main__":
    s = "abc\\p\""
    print("No of words : ", countWords(s))

#Q,10 write a code to concatenate two string without using + oprator

str1 = "pw"
str2 = "forskills"
 
# join() method is used to combine the strings
print("".join([str1, str2]))
 
# join() method is used here to combine 
# the string with a separator Space(" ")
str3 = " ".join([str1, str2])
 
print(str3)


#Q.11 write a code to remove all accurrences of specific eliment from a list


    #Q.12 impliment a code to find the second largest number in a given list of intigers  

list1 = [10, 20, 4, 45, 99]
 
mx = max(list1[0], list1[1]) 
secondmax = min(list1[0], list1[1]) 
n = len(list1)
for i in range(2,n): 
    if list1[i] > mx: 
        secondmax = mx
        mx = list1[i] 
    elif list1[i] > secondmax and \
        mx != list1[i]: 
        secondmax = list1[i]
    elif mx == secondmax and \
        secondmax != list1[i]:
          secondmax = list1[i]
 
print("Second highest number is : ",\
      str(secondmax))

#q.13 creat a code to count the occurrences of each 
# eliment in a list and return a dictionary with eliment as keys and 
# thier counts value?

# Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,
                                        countX(lst, x)))


#Q.14 write a code to revrse a list in place without using any built in reverse function

# Reversing a list using slicing technique
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

#Q.15  impliment a code to find and remove duplicates from a 
# list while preserving the original order of eliments

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "
        + str(test_list))

# using set() to remove duplicated from list
test_list = list(set(test_list))

# printing list after removal
# distorted ordering
print ("The list after removing duplicates : "
        + str(test_list))

#q.16 creat a code to cheack if a given list is sorted
# ( either in accending or deccending order )or not

# initializing list
test_list = [10, 4, 5, 8, 10]
 
# printing original list 
print ("Original list : " + str(test_list))
 
# using sort() to 
# check sorted list 
flag = 0
test_list1 = test_list[:]
test_list1.sort()
if (test_list1 == test_list):
    flag = 1
     
# printing result
if (flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")


    #Q.17 write a code to merge two sorted list into a single a sorte list 

    # initializing lists
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
 
# printing original lists 
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))
 
# using sorted()
# to combine two sorted lists
res = sorted(test_list1 + test_list2)
 
# printing result
print ("The combined sorted list is : " + str(res))

#q.18 impliment a code to find the intersection for two given list

# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
 
# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))

#q,19 create a code to find union of two given list

 #Python program to illustrate union
# Maintained repetition 
def Union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list
 
# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))

#q.20 write a code to shuffle a given list randomly without 
# using any built in shuffle function

import random
 
my_list = [1, 2, 3, 4, 5]
 
shuffled_list = sorted(my_list, key=lambda x: random.random())
 
print("Original list:", my_list)
print("Shuffled list:", shuffled_list)


#Q.21 write a code to takes two tuples as input and 
# returns a new tuple containig eliment that are common to both input tuples

# initializing tuples
test_tuple1 = (4, 5)
test_tuple2 = (7, 8)
 
# printing original tuples
print("The original tuple 1 : " + str(test_tuple1))
print("The original tuple 2 : " + str(test_tuple2))
 
# All pair combinations of 2 tuples
# Using list comprehension
res =  [(a, b) for a in test_tuple1 for b in test_tuple2]
res = res +  [(a, b) for a in test_tuple2 for b in test_tuple1]
 
# printing result 
print("The filtered tuple : " + str(res))

#q.22 create a code to that prompts the ussers to eniter two sets of integegers 
# seprated by commas then print the intersection of these two sets

set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {4, 6, 8}
# intersection of two sets
print("set1 intersection set2 : ",
      set1.intersection(set2))
 
# intersection of three sets
print("set1 intersection set2 intersection set3 :",
      set1.intersection(set2, set3))

#Q.23 write a code to concatenates two tuples the function should take two tuples
#  as input and return a new tuple containing eliments from both input tuples

# initialize tuples
test_tup1 = (1, 3, 5)
test_tup2 = (4, 6)
 
# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
 
# Ways to concatenate tuples
# using + operator
res = test_tup1 + test_tup2
 
# printing result
print("The tuple after concatenation is : " + str(res))

#Q.24 develop a code that propts the user to input two sets of string 
# then print the eliment that are present in the frist set but not in the second set

# string 1
a = "pwforskills"
 
# string 2
b = "skills"
 
# convert string 1 into set
setA = set(a)
 
# convert string 2 into set
setB = set(b)
 
# store the difference in form of list
result = setA-setB
 
# print result
print(result)

#Q.25 creat a code that takes a tuple and two intigers as input the function 
# should returns a new tuple containing eliment from the original tuple within the 
# specified range of indices

# creating a list
list1 = [1, 2, 5, 6]
 
# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, val**3) for val in list1]
 
# print the result
print(res)

#Q.26 write a code that prompts the user 
# to input two sets of charcter then print the union of these two sets

set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {7, 8, 9, 10}
 
# union of two sets
print("set1 U set2 U set3 :", set1.union(set2).union(set3))
 
# union of three sets
print("set1 U set2 U set3 :", set1.union(set2, set3))


#Q.27 develope the code that takes a tupel of intigers as input the
#  function should return the maximum and minimum values from the tuple
#  using tuple unpacking

# this lines PACKS values
# into variable a
a = ("MNNIT Allahabad", 5000, "Engineering")  
 
# this lines UNPACKS values
# of variable a
(college, student, type_ofcollege) = a  
 
# print college name
print(college)
 
# print no of student
print(student)
 
# print type of college
print(type_ofcollege)

#Q,28 creat a code that defines two sets of integers then print the 
# union intersection and diffrence of these two sets

# sets are define 
A = {0, 2, 4, 6, 8}; 
B = {1, 2, 3, 4, 5}; 
  
# union 
print("Union :", A | B) 
  
# intersection 
print("Intersection :", A & B) 
  
# difference 
print("Difference :", A - B) 
  
# symmetric difference 
print("Symmetric difference :", A ^ B) 

#Q.29 write a code that takes a tuple and an eliment as
#  input the function should returns the counts of occurrences of the given eliment in tuple

# Program to count the number of times an element
# Present in the list
 
 
def countX(tup, x):
    count = 0
    for ele in tup:
        if (ele == x):
            count = count + 1
    return count
 
 
# Driver Code
tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8
 
print(countX(tup, enq))
print(countX(tup, enq1))
print(countX(tup, enq2))


#Q.29 develop the code that prompts the user input two sets of string then
#  print the symmetric diffrence of these two sets

setA= input("enter set a")
setB= input("enter set b")
print(setA.symmetric_difference(setB))

#Q>31  write a code that takes a list of words as input and return a dictionary where the keys 
# are unique words and the value are the frequinces of those words in the input list

def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print("% d : % d" % (key, value))
 
 
# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
 
    CountFrequency(my_list)

#Q.32 write a code that takes two dictinoary as input and merges them into
#  single dictionary if where are common keys the values should be added together

# Python program to combine two dictionary
# adding values for common keys
# initializing two dictionaries
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'pw': 100, 'skills': 200, 'for': 300}
 
# adding the values with common key
for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass
         
print(dict2)

#Q.33 write a code to acces a value in a nested dictionary the function should take the 
# dictionary and a list os keys as input and return the corresponding value if any of the 
# keys do not exits in the dictionary the function should return none


# Using nested get()
 
# initializing dictionary
test_dict = {'Gfg' : {'is' : 'best'}}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# using nested get()
# Safe access nested dictionary key
res = test_dict.get('Gfg', {}).get('is')
 
# printing result
print("The nested safely accessed value is :  " + str(res))

#Q.34 write a code that takes a dictionary as input and returns a
#  sorted version of it bassed on the values you can choose whetwer to 
# sort in accending order

myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)

#Q.35 write a code that inverts a dictionary swapping keys and values ensure that the invented 
# dictionry correctly handlles casses where multiple keys have the same value by storing the key 
# as a list the inverted dictionary

# swap of key and value 
   
# initializing dictionary 
old_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G': 67, 'H': 23}
 
new_dict = dict([(value, key) for key, value in old_dict.items()])
   
# Printing original dictionary 
print ("Original dictionary is : ")
print(old_dict) 
 
print()
 
# Printing new dictionary after swapping keys and values
print ("Dictionary after swapping is :  ") 
print("keys: values")
for i in new_dict:
    print(i, " :  ", new_dict[i])

    