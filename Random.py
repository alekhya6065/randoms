# Print All Duplicate Characters in a String
# j=input("Enter a string:")
# for i in j:
#     if j.count(i)>1:
#         print(i)
# Replace Vowels with ‘*’
# a=input("Enter a string:")
# vowels="aeiouAEIOU"
# res=""
# for s in a:
#     if s in vowels:
#         res += "*"
#     else:
#         res += s
# print(res)
# Convert a Snake_Case String to CamelCase.
# s= input("Enter snake_case:")
# p=s.split("_")
# camel=""
# for i in p:
#     camel=camel+i[0].upper()+i[1:]
# print("CamelCase:",camel)
# Use reduce() to Find Product of List Elements
from functools import reduce
c=[10,20,30,40,50,60,70,80,90]
result=reduce(lambda a,b:a+b,c)   
print(result)