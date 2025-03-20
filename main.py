import turtle
import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("black")

t=turtle.Turtle()
# menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("Background Color", font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor("tan")
t.write("1. Tan", font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor("azure")
t.write("2. azure" , font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor("AquaMarine")
t.write("3. AquaMarine", font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor("DarkKhaki")
t.write("4.DarkKhaki", font=("arial",20,"normal"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor("white")
t.write("Select a Color", font=("arial",30,"normal"),align="center")

choose = int(input("Select a color: "))
if choose == 1:
    screen.bgcolor("Tan")
elif choose == 2:
    screen.bgcolor("Azure")
elif choose == 3:
    screen.bgcolor("AquaMarine")
else :
    screen.bgcolor("DarkKhaki")

t.clear()

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("black")
t.write("Enter your name: ", font=("arial",30,"normal"),align="center")



name=input("Enter your name: ")
t.clear()
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
operation =  random.randint(1,4)
if operation == 1:
    symbol = "+"
    num1 = random.randint(-100,100)
    num2 = random.randint(100,100)
    solution = num1 + num2

elif operation == 2:
    symbol = "-"
    num1 = random.randint(-100,100)
    num2 = random.randint(100,100)
    solution = num1 - num2

if operation == 3:
    symbol = "*"
    num1 = random.randint(-10,10)
    num2 = random.randint(-10,10)
    solution = num1 * num2

if operation == 4:
    symbol = "/"
    num1 = random.randint(-100,10)
    num2 = random.randint(1,10)
    sign = random.randint(1,-2)
    if sign == 2:
        num2 = -1 + num2
    solution = num1 / num2



t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("blue")
t.write(name, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor("black")
t.write(symbol, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("green")
t.write(num1, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("purple")
t.write(num2, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("black")
t.write(" = ", font=("arial",30,"normal"),align="center")

ans = float(input("Enter the answer"))

t.penup()
t.goto(200,0)
t.penup()
t.pendown()
t.pencolor("red")
t.write(solution, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,-100)
t.penup()
t.pendown()
t.pencolor("black")
t.write("Your answer: " +str(ans), font=("arial",30,"normal"),align="center")

if ans==solution:
    screen.bgcolor("dodgerblue")

    t.penup()
    t.goto(0,50)
    t.penup()
    t.pendown()
    t.pencolor("black")
    t.write("Correct ", font=("arial",30,"normal"),align="center")

else:
    screen.bgcolor("Dark orange")
    t.penup()
    t.goto(0, 50)
    t.penup()
    t.pendown()
    t.pencolor("black")
    t.write("Incorrect ", font=("arial", 30, "normal"), align="center")





turtle.done()
