from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.text", mode= "r") as data:
            data = data.read()
            self.highscore = data.text()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.write(f"Score={self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over. Score: {self.score}. High score: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score == 0
        with open("data.text", mode= "w") as data:
            data = data.write(f"{self.highscore}")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score={self.score}", False, align="center", font=("Arial", 10, "normal"))
