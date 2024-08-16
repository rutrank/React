# '#Q1
# def prime(n):
#   i = 2
#   pm=1

#   while i*i <= n:
#     if n%i==0:
#       pm=i
#       n //=i
#     else:
#       i +=1
#   if n>1:
#     pm=n
#   return pm 
   
# print(prime(36))
 

# #Q2
# n=int (input("enter the number till series "))

# fiblist=[0,1]
# for i in range(0,n):
#   fiblist.append(fiblist[i]+fiblist[i+1])
# print(fiblist)

# for u in range(2,len(fiblist)):
#   gratio=fiblist[u]/fiblist[u-1]

# print(gratio)  

# #Q3

# str = input("enter").lower()
# count=len(str.split())
# words=str.split()

# word_F={}

# for word in words :
#   if word in word_F:
#     word_F[word] +=1
#   else:
#     word_F[word]=1

# for freq,wor in word_F.items():
#   print(f"{freq}:{wor}")

# #Q5
# numbers=[]
# n= int(input("size"))

# for i in range (0,n):
#   z=int(input("enter element"))
#   numbers.append(z)
# print(numbers)

# #Q6
# employee = {}

# while true :
 
#  print("1. Create /n 2. Add /n 3. Search /n 4. Delete /n 5. Display ")
#  choice=int(input("Enter your choice"))
#  employee_details=[]
#  if choice==1:
#   emp_id=int(input("id pl"))

#   employee[emp_id]=employee_details


str="rutrank is a boy"
if "is" in str:
  print("yes")
else:
  print("no")