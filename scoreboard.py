from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def increase_score(self):
        self.current_level += 1
        self.update_score()

    def GAME_OVER(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
