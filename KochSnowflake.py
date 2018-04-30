from turtle import *
speed(10)
penup()
goto(-200, 200)
pendown()
color("red")
def koch(side, step):
    if step > 0:
        koch(side / 3, step - 1)
        right (60)
        koch(side / 3, step - 1)
        left (120)
        koch(side / 3, step - 1)
        right (60)
        koch(side / 3, step - 1)
    else:
        forward(side)
for i in range(6):
    koch (240,4)
    right (60)



