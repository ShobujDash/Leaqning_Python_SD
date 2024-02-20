# str1 = "This is a sting."
# len1 = len(str1)
# print(len1)
# str2 = 'Shobuj'
# print(len(str2))
# str3 = """This is a string"""


# str = "This is a string. \nwe are creteing it in python"
# print(str)



# concatination
# print(str1 + " " + str2)



# Indexing
# Shobuj Das
# 0123456789

# str = "apna college"
# ch = str[9]
# print(ch);




# Slicing
# Accessing parts of a string
# str[starting_index: ending_index]

# Negative Index
#  A  P  P  L  E
# -5 -4 -3 -2 -1

# str = "ApnaCollege"
# slice = str[0:4];
# sliceNew = str[:4];
# slice1 = str[4:len(str)]
# slice2 = str[4:]
# print(sliceNew)
# print(slice)
# print(slice1)
# print(slice2)






# String Fucntions
# str = "i am from studing python from Apna college"

# str1 = str.endswith("ege") #returns true if strign ends with substr
# print(str.endswith("ppp"))
# print(str1)

# str = str.capitalize() #capitalize 1st charecter
# print(str);

# print(str.replace("python","javascript"))

# print(str.find("studi"))
# print(str.find("Q"))

# print(str.count("from"))
# print(str.count("o"))






#Let's Practice 
# WAP to input user's first name & print its length
# WAP to find the occurrence of '$' in a string

# name = input("enter your name : ")
# print("length of your name is : ", len(name))

# str = "Hi, $I am the $$ symbol $99.99"
# print(str.count("$"))


# Conditional Statements
# if-elif-else (SYNTAX)
# if(conditin):
#   Statement1
# elif(condition)
#   Statement2
# else:
#   StatementN

# light = "yellossw"
# if(light == "red"):
#   print("stop") #indentation{}
# elif(light == "green"):
#   print("go")
# elif(light == "yellow"):
#   print("look")
# else:
#   print("light is broken")

# print("end of code");

  
# marks= int(input("enter student marks : "))

# if(marks >= 90):
#   grade = "A"
# elif(marks >= 80 and marks < 90):
#   grade = "B"
# elif(marks >= 70 and marks < 80):
#   grade= "C"
# else:
#   grade = "D"

# print("grade of the student =>", grade)




# Let's Practice
# WAP  to find the greates of 3 numbers entered by the user 
a = int(input("enter first number : "))
b = int(input("enter second number : "))
c  = int(input("enter third number : "))
if(a>=b and a>=c):
  print("A grater then b and c", a)
elif(b >=c):
  print("second number is lagest",b)
else:
  print("third is larget",c)