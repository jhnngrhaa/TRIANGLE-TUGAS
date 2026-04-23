import turtle

def draw_3d_triangle() -> None:
    screen = turtle.Screen()
    screen.title("Segitiga 3D di Canvas")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(2)
    t.color("black")
    t.speed(3)
    
    t.fillcolor("blue")
    t.begin_fill()
    t.goto(0, 300)
    t.goto(-200, -100)
    t.goto(0, -180)
    t.goto(0, 300)
    t.end_fill()

    t.fillcolor("darkblue")
    t.begin_fill()
    t.goto(0, 300)
    t.goto(200, -100)
    t.goto(0, -180)
    t.goto(0, 300)
    t.end_fill()

    screen.mainloop()

if __name__ == "__main__":
    draw_3d_triangle()
