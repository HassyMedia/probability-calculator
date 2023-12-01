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

# The experiment function: Conducts a specified number of experiments to calculate the probability.
# This function takes a Hat object, an expected ball distribution, number of balls to draw, and number of experiments.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0  # Initialize a count of successful experiments.
    for _ in range(num_experiments):
        # Create a copy of the hat for each experiment to preserve original contents.
        experiment_hat = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = experiment_hat.draw(num_balls_drawn)  # Draw balls from the hat.
        # Check if the drawn balls meet the expected distribution.
        if all(drawn_balls.count(color) >= count for color, count in expected_balls.items()):
            success_count += 1  # Increment the success count if the experiment meets expectations.
    return success_count / num_experiments  # Return the probability based on the number of successful experiments.
