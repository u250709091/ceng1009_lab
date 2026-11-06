# ---------- Exercise 1 --------------- #

# def market(x):
#     if x >= 90:
#         return "A"
#     elif x >= 80:
#         return "B"
#     elif x >= 70:
#         return "C"
#     elif x >= 60:
#         return "D"
#     else:
#         return "F"
#
# note = int(input("A değerini giriniz :"))
# print(market(note))


# ---------- Exercise 2 --------------- #


# import turtle
#
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def drawBar(t, height, gap):
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.write(" " + str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height = max(data)
#     num_bars = len(data)
#     border = 10
#     gap = (max_height + border) / 25
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars + border
#     top = max_height + 4 * border
#     wn.setworldcoordinates(-border, -border, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
#     wn.exitonclick()
#
#
# data = [40,117,200, 240, 160, 260, 220]
# barChart(data)




# ---------- Exercise 3 --------------- #


# import turtle
#
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def drawBar(t, height, gap):
#
#     if (height >= 0):
#         labelY = height + gap
#     else:
#         labelY = gap
#
#
#     t.penup()
#     t.left(90)
#     t.forward(labelY)
#     t.write(" " + str(height))
#     t.backward(labelY)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height = max(data)
#     min_height = min(data)
#     num_bars = len(data)
#     border = 10
#     gap = (max_height + border) / 25
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars + border
#     top = max_height + 4 * border
#     bottom = min(min_height, 0) - border
#     wn.setworldcoordinates(-border, bottom, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
#     wn.exitonclick()
#
#
# data = [40,117,-60, 10, 160, -120, 220]
# barChart(data)




# ---------- Exercise 4 --------------- #


# import math
#
# def findHypot(a, b):
#     hypot = (a ** 2 + b ** 2) ** 0.5
#     return hypot
#
# def calcWithMath(a, b):
#     hypot = math.sqrt (a ** 2 + b ** 2)
#     return hypot
#
# print(findHypot(3, 4))
# print(calcWithMath(3, 4))


