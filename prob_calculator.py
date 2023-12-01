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

    # The draw method: Draws a specified number of balls randomly from the hat.
    # If the number of balls to draw exceeds the available quantity, it draws all the balls.
    def draw(self, number):
        number = min(number, len(self.contents))  # Adjust the number if it exceeds the available balls.
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(number)]  # Randomly draw and remove balls from the hat.
