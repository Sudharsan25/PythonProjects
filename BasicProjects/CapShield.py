# from turtle import *
# color('green')
# bgcolor('black')
# speed(11)
# hideturtle()
# b = 0
# while b < 200:
#     right(b)
#     forward(b * 3)
#     b = b+1

# from turtle import *
# bgcolor("black")

# speed(0)
# pensize(4)
# pencolor("blue")

# def draw_circle(radius):
#     for i in range(10):
#         circle(radius)
#         radius = radius - 4

# def draw_design():
#     for i in range(10):
#         draw_circle(150)
#         right(36)
    
# draw_design()
# done()

from turtle import *
bgcolor('white')
pensize(2)

up()
goto(0,-200)
down()
pencolor('red')
fillcolor('red')
begin_fill()
circle(200)
end_fill()

up()
goto(0,-150)
down()
pencolor('black')
fillcolor('white')
begin_fill()
circle(150)
end_fill()

up()
goto(0,-100)
down()
pencolor('black')
fillcolor('red')
begin_fill()
circle(100)
end_fill()

up()
goto(0,-50)
down()
pencolor('black')
fillcolor('blue')
begin_fill()
circle(50)
end_fill()

up()
goto(1,-30)
down()
color("white")
left(72)
begin_fill()
for i in range(5):
    forward(72)
    left(144)

end_fill()
hideturtle()
done()
