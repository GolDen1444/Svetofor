from turtle import *

def trunk():
    color('brown')
    penup()
    goto(0,-150)
    pendown()
    pensize(20)
    left(90)
    forward(200)
def leaves():
    pensize(10)
    color('green')
    count = 10
    for _ in range(26):
        forward(count)
        count += 5
        left(90)

trunk()
leaves()
hideturtle()
exitonclick()
