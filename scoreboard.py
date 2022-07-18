from turtle import Turtle

font = ('Arial', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", False, "center", font)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", font)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font)
