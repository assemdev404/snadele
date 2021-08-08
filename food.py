from turtle import Turtle
import random


class Food(Turtle):
    """You Hungry? I've got you some random blue bits for your snake.
    Feed them to it, then eat it! Quite a plan... I know."""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        """blazing fast blinking function used to teleport the food
        away from the snake once He reaches it;
        He would still think he ate it and get bigger each time."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
