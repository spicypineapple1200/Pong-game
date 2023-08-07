import turtle as t


class Paddle(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shapesize(5, 1)
        self.speed(0)
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)