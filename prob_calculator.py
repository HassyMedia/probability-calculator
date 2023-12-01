import random

class Hat:
    # Constructor: Initializes a new instance of the Hat class.
    # Accepts variable keyword arguments (**balls) representing different colored balls.
    # Each key is the color of the ball, and the corresponding value is the count of that ball.
    def __init__(self, **balls):
        self.contents = []  # Initialize an empty list to hold the balls.
        for color, count in balls.items():
            # For each color, add the appropriate number of balls to the contents list.
            self.contents.extend([color] * count)
