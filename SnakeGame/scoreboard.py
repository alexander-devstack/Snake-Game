from os import write
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score:{self.high_score}", False, "center",
                   ('Comic Sans MS', 15, 'normal'))

    def score_count(self):
        self.score += 1
        self.update_scoreboard()

