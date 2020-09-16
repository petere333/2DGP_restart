import turtle as t

t

for x in range(0,5):
    for y in range(0,5):
        t.penup()
        t.goto(x*100,y*100)
        t.pendown()
        for i in range(0,4):
            t.forward(100)
            t.left(90)

t.exitonclick()