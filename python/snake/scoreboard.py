from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
FILE_PATH = "/Users/heyjamal/Downloads/python/snake/data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(FILE_PATH, "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH, "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
