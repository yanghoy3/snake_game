from turtle import Turtle

import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.6, 0.6)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)




