import turtle
from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
turtle.colormode(255)


def random_color():
    """Your eyes are strained? Good. Let's fuck 'em even more."""
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


class Snake:
    """Sick of fancy games? Don't know what to do with your life?
    Have Been considering suicide lately? Couldn't find the True purpose of your life!
    Well... not anymore. I've got you THE SNAKE!
    The only true thing in a our virtual world."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """It's not as poisonous as Humans tho, Don't worry."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """No idea what segment mean. If you know comment it here, then push a commit."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Don't use it on your ego, We've had enough of you already."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """You snaky bastard!"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].color(random_color())
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[seg_num].speed('fastest')
        self.segments[0].forward(20)

    def up(self):
        """Did you know 'up' in Arabic means father."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """No not mother."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Turnips... Lol, like turn up, but multiple times"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """?"""
        if self.head.heading() != 180:
            self.head .setheading(0)
