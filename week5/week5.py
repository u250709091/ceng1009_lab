# import random
#
# for i in range(10):
#     print(random.random())



# import random
#
# for i in range(10):
#     print(random.randint(25,35))



# import math
#
# hypotenuse = math.hypot(3,4)
# print(hypotenuse)


# import math
#
# a = int(input("Enter length: "))
# b= int(input("Enter width: "))
# hypotenuse = math.sqrt(a**2 + b**2)
# print(hypotenuse)


# import math
#
# def areaOfCircle(radius):
#     return math.pi * (radius ** 2)
# print(areaOfCircle(5))



# import turtle
#
# def drawStart(t,side):
#
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# screen = turtle.Screen()
# tess = turtle.Turtle()
#
# drawStart(tess,100)
# screen.exitonclick()
#

#
# import turtle
#
# def drawSquare(t, side):
#
#     for i in range(4):
#         t.forward(side)
#         t.left(90)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor("lightyellow")
# tess.color("purple")
# tess.pensize(4)
#
# for i in range(5):
#     drawSquare(tess, 30)
#     tess.penup()
#     tess.forward(60)
#     tess.pendown()
#
#
# screen.exitonclick()



# import turtle
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor("yellow")
# tess.color("purple")
# tess.pensize(4)
#
# def drawSquare(t, side):
#
#     for i in range(5):
#         t.forward(side)
#         t.left(90)
#
# for i in range(20,120,20):
#     drawSquare(tess, i)
#     tess.penup()
#     tess.backward(10)
#     tess.right(90)
#     tess.forward(10)
#     tess.left(90)
#     tess.pendown()
#
# screen.exitonclick()











