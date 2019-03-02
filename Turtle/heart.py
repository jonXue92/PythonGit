# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 23:33:23 2018

@author: 薛正扬
"""

import turtle
import math

wn=turtle.Screen()
wn.setworldcoordinates(-2,-2,2,2)
turtle.penup()
i=-1
while i<=0:
    y1=math.sqrt(1-i*i)+(i*i)**(1/2.0)
    turtle.setx(i)
    turtle.sety(y1)
    turtle.dot()
    i+=0.01

import turtle
import time
def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
love=input('Please enter a sentence of love,otherwise the default is "I Love You":\n')
me=input('Please enter pen name, otherwise the default do not execute:\n')
if love=='':
    love='I Love you'
turtle.setup(width=900, height=500)
turtle.color('red','pink')
turtle.pensize(3)
turtle.speed(5)
turtle.up()
turtle.hideturtle()
turtle.goto(0,-180)
turtle.showturtle()
turtle.down()
turtle.speed(5)
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
LittleHeart()
turtle.left(120)
LittleHeart()
turtle.forward(224)
turtle.end_fill()
turtle.pensize(5)
turtle.up()
turtle.hideturtle()
turtle.goto(0,0)
turtle.showturtle()
turtle.color('#CD5C5C','pink')
turtle.write(love,font=('Times',30,'bold'),align="center")
turtle.up()
turtle.hideturtle()
if me !='':
    turtle.color('black', 'pink')
    time.sleep(2)
turtle.goto(180,-180)
turtle.showturtle()
turtle.write(me, font=('Times',20,'normal'), align="right", move=True)
window=turtle.Screen()
window.exitonclick()


import turtle
 
turtle.title('领导专用程序')
lv=turtle.Turtle()
lv.hideturtle()
lv.getscreen().bgcolor('light blue')
lv.color('yellow','red')
lv.pensize(1)
lv.speed(1)
lv.up()
lv.goto(0,-150)
#开始画爱心
lv.down()
lv.begin_fill()
lv.goto(0, -150)
lv.goto(-175.12, -8.59)
lv.left(140)
pos = []
for i in range(19):
    lv.right(10)
    lv.forward(20)
    pos.append((-lv.pos()[0], lv.pos()[1]))
for item in pos[::-1]:
    lv.goto(item)
lv.goto(175.12, -8.59)
lv.goto(0, -150)
lv.left(50)
lv.end_fill()
#写字
lv.up()
lv.goto(0, 80)
lv.down()
lv.write("美女",font=(u"方正舒体",36,"normal"),align="center")
lv.up()
lv.goto(0, 0)
lv.down()
lv.write("新年快乐！",font=(u"方正舒体",48,"normal"),align="center")
lv.up()
lv.goto(100, -210)
lv.down()
lv.write("点我点我快点我",font=(u"华文琥珀",26,"bold"),align="right")
lv.up()
lv.goto(160, -190)
lv.resizemode('user')
lv.shapesize(4, 4, 10)#调整小乌龟大小，以便覆盖“点我”文字
lv.color('red', 'red')
lv.showturtle()