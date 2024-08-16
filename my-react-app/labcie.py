# n = int(input("Enter the number"))
# n = int(n)
# maxPrime = -1
# while n%2==0:
#   maxPrime = n
#   n=n/2
#   print("N:" , n)
# print ("N: ", n)
# for i in range(3,int(n**0.5)+1,2):
#  while n%i==0:
#   maxPrime=i
#   n=n/i
#  if n>2 :
#   maxPrime = n
#   print("Max Prime Factor :" , int(maxPrime))


str = "My name is Rutrank Tandon. I study in RVCE"
print("Entered Paragraph is:", str)
wordCount = len(str.split())
print("Total number of words:", wordCount)

counts = dict()
words = str.split()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print("Word counts:", counts)

searchWord = input("Enter the word to be searched: ")
result = str.find(searchWord)
if result != -1:
    print(searchWord, "Yes")
else:
    print(searchWord, "No")
