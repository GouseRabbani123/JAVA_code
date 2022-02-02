#practice

a = int(input())
students_marks = {}
for i in range(a):
    name,*score = input(),split()
    scores = list(map(float,score())
    students_marks[name]=scores
b = input()
c = student_marks[b]
sum = 0
for j in (b):
    sum=sum+1
    avg=sum/3
print("{0.2f}".format(avg))

a = int(input())
student_marks = {}
for i in range(a):
    b=name,*score = input().split()
    scores = list(map(float,score))
    student_marks[name] = scores
c = input()
d = student_marks[c]
sum = 0;
for j in (d):
    sum = sum+j
    avg = sum/3
print("{0:.2f}".format(avg))
























#FINDING THE PERCENTAGE
#SAMPLE INPUT
# 3
# GOUSE 67 68 69
# SHAHIB 7 98 63
# MALIKA 52 56 60
# MALIKA

# SAMPLE OUTPUT
# 52+56+60/3
# =56.00

# CODE

N = int(input())
students_marks={}
for i in range(N):
    name, *line = input().split()#this line is for  getting the values 
    # like this
    # harsh 25 26.5 28
    # anurag 26 28 30
    # print(name)
    # print(line) here print  line and name will  gives this output
    # Krishna
    # ['67', '68', '69']
    # Arjun
    # ['70', '98', '63']
    # Malika
    # ['52', '56', '60']

    
    scores = list(map(float,line))
   # print(scores)
   # this above line collets all the score value like  this althrough they are in float models
    #[67.0, 68.0, 69.0]
   #[70.0, 98.0, 63.0]
   #[52.0, 56.0, 60.0]
   
   
   

#here am storing the  scores value in student_marks
#print(student_marks)  in this dictionary we are storing this values of name  and marks of the studeents
# //like this
# Krishna
# ['67', '68', '69']
# Arjun
# ['70', '98', '63']
# Malika
# ['52', '56', '60']

#To get only the scores but not the name write  this line of code
student_marks[name] = scores#inside  this we get only the scores like this
# print(students_marks[name]:
# output = 
# [67.0, 68.0, 69.0]
# [70.0, 98.0, 63.0]
# [52.0, 56.0, 60.0]




query_name = input()
#this above line is used  for giving the nme for which we need to find out the answer 
s = 0
for j in student_marks[query_name]:#here in this "student_marks[query_name]" we are getting the values inside the given name 
    s=s+i#here we are  aadding  the values with one another inside the loop
print("{0:2f}".format(s/3))#from thie line we can  GET THE FINAL OUTPUT WITH ROUND OF 2 DECMAL FLOAT VALUES

# here {0:2f}
# means 0 is the number before the point 2f means float values after the .
# example:0.25











    
    
    
    
    
    
    
    
    
    
    
    
 # use of format
 #named indexes:
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# #numbered indexes:
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# #empty placeholders:
# txt3 = "My name is {}, I'm {}".format("John",36)

# print(txt1)
# print(txt2)
# print(txt3)
    
 # output =    my name is John,  I'm 36
 # output =    my name is John,  I'm 36
 # # output =    my name is John,  I'm 36


# SAMPLE  CODE WITHOUT COMMENTS
# n = int(input())
# student_marks = {}
# for i in range(n):
    # x = name,*score = input().split()
    # # print(name)
    # # print(score)
    # scores= list(map(float,score))
    # # print(scores)
    # student_marks[name]= scores
    # #print(student_marks[name])
# z = input()
# y =(student_marks[z])
# sum=0
# for j in y:
    # sum+=j
    # avg=sum/3
# print("{0:.2f}".format(avg))    
    
    
      
   

