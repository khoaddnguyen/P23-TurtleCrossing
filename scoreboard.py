from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Level {self.score}", align=ALIGNMENT, font=FONT )
