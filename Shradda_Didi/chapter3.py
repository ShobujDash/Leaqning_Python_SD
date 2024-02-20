# Lists in Python
# A build-in data type that store set of values 
# it can store elements of different types (integer, float , string , etc...)



# marks1 = 94.4
# marks2 = 87
# marks3 = 95

# marks = [94,4, 87.5, 94.3, 66.4, 45.1]


# print(marks)
# print(type(marks))
# print(len(marks))

# print(marks[0])
# print(marks[1])



# string ------> immutable
# list --------> mutable

# string ------> immutable
# str = "hello"
# print(str[0])
# str[0] = "y"  # it's not will be change

# list --------> mutable
# students = ["Shobuj",23,95.5,"Laksam"]
# print(students[0])
# students[0] = "DasBabu"
# print(students)




# List Slicing
# Similar to String Slicing

# students = ["Shobuj",23,95.5,"Laksam"]
# print(students[1:4])
# print(students[1:])
# print(students[:3])





# List Methods 
# list = [2,1,3,4,5,6]

# new = list.append(5)
# print(new)
# print(list)

# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)

# list.remove(4)
# print(list)

# list.pop()
# print(list)

# list.clear()
# print(list)





















#### Tuples in Python 
# A built-in data type that lets us create immutable sequences of values
# Just like strings

# tup = (2,3,4,5,1)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# print(tup[2])





# Let's Practive
# 1) Write a program to ask the user to enter names of their 3 favorite movies & store them in a list 

# solve type 01
# movies = []
# mov1 = input("enter 1st movie : ")
# mov2 = input("enter 2nd movie : ")
# mov3 = input("enter 3rd movie : ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# Solve type 02
# movies = []
# movies.append(input("enter 1st movie : "))
# movies.append(input("enter 2nd movie : "))
# movies.append(input("enter 3rd movie : "))
# print(movies)


# 2) Write a program t check if a list cntins a palindrome of elements.(Hint:use copy() method)
# maam
# racecar

# list1 = [1,2,3,2,1]
## list1 = [1,2,3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(list1 == copy_list1):
#   print("palindrom")
# else:
#   print("Not Palindrom")



# 3) WAP  to count the number of stuendts with the "A" grade in the following tuple.
# ["C","D","A","A","B","B","A"]
# Store the above values in a list & sort then from "A" to "D"

# grade = ("C","D","A","A","B","B","A")
# print(grade.count("A"))

# grade = ["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)