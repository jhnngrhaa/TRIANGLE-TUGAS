import turtle

def draw_triangle(side_length: int) -> None:
    screen = turtle.Screen()
    screen.title("Segitiga di Canvas")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.hideturtle()
    t.color("black")
    t.fillcolor("red")
    t.pensize(3)
    
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()
    
    screen.mainloop()

if __name__ == "__main__":
    draw_triangle(400)
