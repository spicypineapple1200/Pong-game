import turtle as t


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1