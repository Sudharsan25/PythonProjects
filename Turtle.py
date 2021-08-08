import turtle as tu

turtle_obj = tu.Turtle()
screen_obj = tu.Screen()
screen_obj.bgcolor('black')
screen_obj.title("Tree Pattern")

turtle_obj.left(90)
turtle_obj.speed(20000)
def draw(l):
    if(l < 10):
        return
    else:
        turtle_obj.pensize(2)
        turtle_obj.pencolor("yellow")
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(3 *l/4)
        turtle_obj.right(60)
        draw(3*l/4)
        turtle_obj.left(30)
        turtle_obj.pensize(2)
        turtle_obj.backward(l)

draw(20)

turtle_obj.right(90)
turtle_obj.speed(20000)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle_obj.pensize(2)
        turtle_obj.pencolor("magenta")  # magenta
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(3 * l / 4)
        turtle_obj.right(60)
        draw(3 * l / 4)
        turtle_obj.left(30)
        turtle_obj.pensize(2)
        turtle_obj.backward(l)


draw(20)

turtle_obj.left(270)
turtle_obj.speed(20000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle_obj.pensize(2)
        turtle_obj.pencolor("red")  # red
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(3 * l / 4)
        turtle_obj.right(60)
        draw(3 * l / 4)
        turtle_obj.left(30)
        turtle_obj.pensize(2)
        turtle_obj.backward(l)


draw(20)

turtle_obj.right(90)
turtle_obj.speed(20000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle_obj.pensize(2)
        turtle_obj.pencolor('#FFF8DC')  # white
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(3 * l / 4)
        turtle_obj.right(60)
        draw(3 * l / 4)
        turtle_obj.left(30)
        turtle_obj.pensize(2)
        turtle_obj.backward(l)


draw(20)


########################################################

def draw(l):
    if (l < 10):
        return
    else:

        turtle_obj.pensize(3)
        turtle_obj.pencolor("lightgreen")  # lightgreen
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(4 * l / 5)
        turtle_obj.right(60)
        draw(4 * l / 5)
        turtle_obj.left(30)
        turtle_obj.pensize(3)
        turtle_obj.backward(l)


draw(40)

turtle_obj.right(90)
turtle_obj.speed(20000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle_obj.pensize(3)
        turtle_obj.pencolor("red")  # red
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(4 * l / 5)
        turtle_obj.right(60)
        draw(4 * l / 5)
        turtle_obj.left(30)
        turtle_obj.pensize(3)
        turtle_obj.backward(l)


draw(40)

turtle_obj.left(270)
turtle_obj.speed(20000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle_obj.pensize(3)
        turtle_obj.pencolor("yellow")  # yellow
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(4 * l / 5)
        turtle_obj.right(60)
        draw(4 * l / 5)
        turtle_obj.left(30)
        turtle_obj.pensize(3)
        turtle_obj.backward(l)


draw(40)

turtle_obj.right(90)
turtle_obj.speed(20000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle_obj.pensize(3)
        turtle_obj.pencolor('#FFF8DC')  # white
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(4 * l / 5)
        turtle_obj.right(60)
        draw(4 * l / 5)
        turtle_obj.left(30)
        turtle_obj.pensize(3)
        turtle_obj.backward(l)


draw(40)


########################################################
def draw(l):
    if (l < 10):
        return
    else:

        turtle_obj.pensize(2)
        turtle_obj.pencolor("cyan")  # cyan
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(6 * l / 7)
        turtle_obj.right(60)
        draw(6 * l / 7)
        turtle_obj.left(30)
        turtle_obj.pensize(2)
        turtle_obj.backward(l)


draw(60)

turtle_obj.right(90)
turtle_obj.speed(20000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle_obj.pensize(2)
        turtle_obj.pencolor("yellow")  # yellow
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(6 * l / 7)
        turtle_obj.right(60)
        draw(6 * l / 7)
        turtle_obj.left(30)
        turtle_obj.pensize(2)
        turtle_obj.backward(l)


draw(60)

turtle_obj.left(270)
turtle_obj.speed(20000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle_obj.pensize(2)
        turtle_obj.pencolor("magenta")  # magenta
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(6 * l / 7)
        turtle_obj.right(60)
        draw(6 * l / 7)
        turtle_obj.left(30)
        turtle_obj.pensize(2)
        turtle_obj.backward(l)


draw(60)

turtle_obj.right(90)
turtle_obj.speed(20000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        turtle_obj.pensize(2)
        turtle_obj.pencolor('#FFF8DC')  # white
        turtle_obj.forward(l)
        turtle_obj.left(30)
        draw(6 * l / 7)
        turtle_obj.right(60)
        draw(6 * l / 7)
        turtle_obj.left(30)
        turtle_obj.pensize(2)
        turtle_obj.backward(l)


draw(60)
screen_obj.exitonclick()



