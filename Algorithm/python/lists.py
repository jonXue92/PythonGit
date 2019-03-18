# -*- coding: utf-8 -*-

lis = [0, 2, 6, 5, 1]
lis_temp = sorted(lis)
lis.sort(reverse = True)
print(lis_temp)
print(lis)

for index, num in enumerate(lis):
    print("the " + str(index) + " number is " + str(num))
    
friends = ['Alice', 'Bob', 'Kason', 'YY']
friends_temp = []
for friend in friends:
    friends_temp.append("Name:" + friend)
print(friends_temp)

friends_tmp = ["Name:" + friend for friend in friends]
print(friends_tmp)

x = 0
end = 10
sum = 0
while x < end:
    if x % 2 == 0:
        x += 1
        continue
    print(x)
    sum += x
    x += 1
print(sum)

A = ['abc', 'acb', 'abc', 'acc']
while 'abc' in A:
    A.remove('abc')
print(A)

lis = ['Alice', 'Hello', 20, 'Python']
message = slice(1,)
user_name = slice(0,1)
print("User: " + str(lis[user_name]) + " Message: " + str(list[message]))