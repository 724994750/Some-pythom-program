#KochDrawV1.py
import turtle

def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    turtle.speed(10000000)
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(4)
    turtle.pencolor('Blue')
    level=4
    koch(400,level)
    turtle.right(120)
    turtle.pencolor('Red')
    koch(400,level)
    turtle.right(120)
    turtle.pencolor('Green')
    koch(400,level)
    turtle.right(120)
    turtle.hideturtle()

main()
