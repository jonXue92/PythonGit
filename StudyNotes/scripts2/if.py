# -*- coding: utf-8 -*-

height = 1.68
weight = 73

bmi = weight/height/height
if bmi > 32:
    print('Xiao Ming is 严重肥胖')
elif bmi <= 32 and bmi > 28:
    print('Xiao Ming is 肥胖')
elif bmi <= 28 and bmi > 25: 
    print('Xiao Ming is overweight')
elif bmi <= 25 and bmi > 18.5:
    print('Xiao Ming is 正常')
else:
	print('Xiao Ming is 过轻')	