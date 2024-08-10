from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def Move_forward(self):
        self.forward(MOVE_DISTANCE)

    def Move_backward(self):
        self.backward(MOVE_DISTANCE)

    def reached_finish_line(self):
        if self.ycor() > 290:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)
