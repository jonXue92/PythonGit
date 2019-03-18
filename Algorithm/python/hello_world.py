# -*- coding: utf-8 -*-

show_message = 2
print(show_message)

def Hello():
    # global 局部变量， 全局变量
    global show_message
    for i in range(1, 6):
        show_message = "Hello"
        print(show_message + " " + str(i))
        
Hello()
print(show_message)

message = "ljy"
print('Hello %s' %message)

word1 = ' Hello '
print(word1)
word1.lstrip()
print(word1)
word1.rstrip()
print(word1)

print(word1.lstrip())
print(word1.rstrip())
print(word1.lstrip().rstrip())

lis = [0, 1, 2]
lis.append(5)
lis.insert(0, 100)
lis.insert(3, 99)
lis[5] = 7
del lis[4]
print(lis)
lis.pop()
print(lis)
lis.pop(0)
print(lis)
var_a, var_b,var_c = lis
print(str(var_a) + " " + str(var_b) + " " + str(var_c))
lis.append(5)
lis.append(6)
var_a, var_b,var_c, *var_l = lis
print(str(var_a) + " " + str(var_b) + " " + str(var_c))
print(var_l)
var_a, var_b, *var_l, var_c = lis
print(str(var_a) + " " + str(var_b) + " " + str(var_c))
print(var_l)