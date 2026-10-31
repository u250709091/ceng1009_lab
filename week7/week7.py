# # exercise 1
#
# def sumTo(x):
#     y = (x*(x+1))/2
#     return y
#
# n = int(input("give me a number: "))
# print(sumTo(int(n)))
#
#
# # exercise 2
#
# import turtle
#
# def draw_star_if(t, n, size):
#
#     if n >= 3 and n%2 != 0:
#         wn = turtle.Screen()
#         for i in range(n):
#             t.forward(size)
#             t.left(180 - 180/n)
#         wn.exitonclick()
#     else:
#         print("Please give me a number greater  or equal to 3 and an odd number")
#         return
#
#
# sai = turtle.Turtle()
# sai.pensize(3)
# sai.color("purple")
#
# draw_star_if(sai,11, 150)
#
#
# #exercise 3
#
# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
#
# print(sumTo(3))
#
# x = int(input("Give me a number:"))
# print(sumTo(x))
#
#
# # exercise 4
#
# import math
#
# def mySqrt(n):
#     x = n/2
#     for i in range (50):
#         newguess = 0.5 * (x + n/x)
#         x = newguess
#     return x
#
# number = int(input("Give me a number to find its square root: "))
# print("This is my function" ,mySqrt(number))
# print("This is math.sqrt function" ,math.sqrt(number))
#
#
# # exercise 5
#
# import turtle
#
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.pencolor("yellow")
# tess.fillcolor("yellow")
#
# wn.bgcolor("purple")
# def draw_mini_triangle(t,size):
#     t.begin_fill()
#     t.rt(90)
#     t.fd(size/24)
#     t.lt(120)
#     t.fd(size/12)
#     t.lt(120)
#     t.fd(size/12)
#     t.lt(120)
#     t.fd(size/24)
#     t.lt(90)
#     t.end_fill()
# def sprite(t,size):
#     for i in range (6):
#         t.fd(size/6)
#         draw_mini_triangle(t,size)
#         t.backward(size/6)
#         t.lt(60)
# def drawSquare(t,size):
#     for i in range(4):
#         t.fd(size)
#         sprite(t,size)
#         t.lt(90)
#
# drawSquare(tess,150)
#
# wn.exitonclick()
#
#
# # # exercise 6
#
# def my_number_is(n):
#     if n==0:
#         y = "Zero"
#     elif n>0:
#         y = "Positive"
#     else:
#         y = "Negative"
#     return y
#
# numbers = [7,-3,0]
#
# for number in numbers:
#     print(number,"is",my_number_is(number))
#
# x = int(input("give me a number:"))
# print(x ,"is",my_number_is(x))
#
#
# #exersice 7
#
# import turtle
#
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height+gap)
#     t.write(" "+str(height))
#     t.backward(height+gap)
#     t.rt(90)
#     t.pendown()
#
#     t.begin_fill()
#     t.left(90)
#     t.fd(height)
#     t.rt(90)
#     t.fd(40)
#     t.rt(90)
#     t.fd(height)
#     t.lt(90)
#     t.end_fill()
#
# def bar(data):
#     maxheight = max(data)
#     num_bars = len(data)
#     border = 10
#     gap = (maxheight-border)/25
#     wn = turtle.Screen()
#     wn.bgcolor("purple")
#
#     right = 40 * num_bars +border
#     top = maxheight +4 * border
#
#     wn.setworldcoordinates(-border,-border,right,top)
#     t = turtle.Turtle()
#     t.color("yellow")
#     t.fillcolor("yellow")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#     wn.exitonclick()
#
# data = [48,117,200,240,160,260,220]
#
# bar(data)