#绘制七位数码管
import turtle,time

def drawGap():#添加数码管空格
    turtle.penup()
    turtle.fd(3)

def drawLine(draw):#绘制直线然后改变方向
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(30)
    drawGap()
    turtle.right(90)
    
def drawDigit(digit):#绘制对应数字的七位数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8,] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(40)

def drawDate(date):#绘制得到的字符
    turtle.pencolor("Red")
    for i in date:
        if i == "-":
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.pencolor("Green")
            turtle.fd(50)
        elif i == "=":
            turtle.write("月",font=("Arial",18,"normal"))
            turtle.fd(40)
        elif i == "+":
            turtle.write("日",font=("Arial",18,"normal"))
            turtle.fd(10)
        else:
            drawDigit(eval(i))
            
def main():#主函数
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.pensize(5)
    turtle.pencolor("Blue")
    turtle.fd(-300)
    drawDate(time.strftime ("%Y-%m=%d+",time.gmtime()))
    turtle.hideturtle()
    turtle.done()

main()
        
