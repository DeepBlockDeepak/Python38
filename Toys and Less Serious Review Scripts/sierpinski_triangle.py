import turtle

pen = turtle.Turtle()

def draw_triangle(length):
    pen.setheading(180)      # set the direction of the pen to left
    for i in range(3):       # draw 3 sides
        pen.rt(120)          # rotate the pen 120 degrees clockwise
        pen.fd(length)       # draw side
                             # pen will end facing left (180)


#draw_triangle(200)

def sierpinksi_order_three_recursive(n, length):
    if n == 1:
        draw_triangle(length)
    else:
        sierpinksi_order_three_recursive( (n - 1) , length)
        pen.rt(120)
        pen.fd(length * (n - 1))
        sierpinksi_order_three_recursive(n -1, length)
        pen.lt(120)
        pen.fd(length * (n - 1))
        sierpinksi_order_three_recursive(n - 1, length)
        pen.fd(length * (n - 1))

sierpinksi_order_three_recursive(1, 300)