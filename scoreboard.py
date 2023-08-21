from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("white")
        self.penup()
        self.hideturtle()

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Level {self.score}", align=ALIGNMENT, font=FONT )

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

