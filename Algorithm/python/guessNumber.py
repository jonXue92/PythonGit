# -*- coding: utf-8 -*-

ans = 9
data_in = int(input("Please input a number: "))
while data_in != ans:
    if data_in > ans:
        print("Too big")
    else:
        print("Too small")
    data_in = int(input("Please input a new number: "))
else:   
    print("Great! You win!")