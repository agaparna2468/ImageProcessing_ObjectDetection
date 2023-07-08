#for item in "Python":
#   print(item)
#for item in range(10):
#   print(item)

#price=[10,30,40]
#sum = 0
#for itr in price:
#   sum += itr
#print(f"Total: {sum}")

#for i in range(1,3):
#   print("*****")
#   for j in range(i):
#       print("**")

#numbers=[5,2,5,2,2]
#for i in numbers:
#    print("*"* i)

numbers = [10,18,10,5,4,4,2,3,1,3,3]

for i in numbers:
    ind = numbers.index(i)
    if ( numbers.count(i) > 1):
        for j in range(numbers.count(i)):
            numbers.remove(i)
        numbers.insert(ind,i)

print(numbers)