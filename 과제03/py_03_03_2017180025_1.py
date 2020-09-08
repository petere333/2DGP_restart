
import turtle as t

t

# 유일하게 공통된 ㄴ자 그리기 함수
def nieun(x,y):
    t.penup()
    t.setheading(0)
    t.goto(x,y)
    t.pendown()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(100)

# ㅇ
t.penup()
t.goto(-200,200)
t.pendown()
t.setheading(0)
t.circle(50)

# ㅠ
t.penup()
t.goto(-300,150)
t.pendown()
t.forward(200)
t.penup()
t.goto(-175,150)
t.right(90)
t.pendown()
t.forward(50)
t.penup()
t.goto(-225,150)
t.pendown()
t.forward(50)

# ㅎ
t.penup()
t.goto(0,300)
t.setheading(0)
t.pendown()
t.forward(50)
t.penup()
t.goto(-25,270)
t.pendown()
t.forward(100)
t.penup()
t.goto(25,200)
t.pendown()
t.circle(20)

# ㅕ
t.penup()
t.goto(50,230)
t.pendown()
t.forward(50)
t.penup()
t.goto(50,210)
t.pendown()
t.forward(50)
t.penup()
t.goto(100,300)
t.right(90)
t.pendown()
t.forward(150)

#ㄴ

nieun(25,150)


# ㅈ
t.penup()
t.goto(250,300)
t.setheading(0)
t.pendown()
t.forward(100)
t.goto(300,300)
t.right(90)
t.forward(30)
t.right(45)
t.forward(30)
t.goto(300,270)
t.forward(40)
t.goto(300,270)
t.left(90)
t.forward(40)

# ㅣ
t.penup()
t.goto(400,350)
t.setheading(0)
t.pendown()
t.right(90)
t.forward(150)

# ㄴ
nieun(300,200)

t.exitonclick()