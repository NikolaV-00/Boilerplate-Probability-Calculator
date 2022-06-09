import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **hat):
        self.contents = list()
        # Each ball will be added to self.contents a number of times
        # depending on the number
        # E.g. "red=2" would be "red", "red"
        for ballColor, numberOfBalls in hat.items():
            self.contents.extend([ballColor] * numberOfBalls)

    def draw(self, numberOfDraws):
        removedBalls = []
        # return all balls if the number of draws
        # is greater than the number of balls
        if numberOfDraws > len(self.contents):
            return self.contents
        else:
            # Remove a number of balls from self.contents based on the
            # numberOfDraws parameter append it to the removedBalls list
            # E.g. a hat has 7 balls, so drawnBall = random number between 1 and 7
            for _ in range(numberOfDraws):
                drawnBall = self.contents.pop(random.randrange(len(self.contents)))
                removedBalls.append(drawnBall)
        return removedBalls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0

    for _ in range(num_experiments):
        # Make a new collection of expected_balls and hat arguments
        # in order to preserve the originals
        expectedBalls = copy.deepcopy(expected_balls)
        hatCopy = copy.deepcopy(hat)
        drawnBalls = hatCopy.draw(num_balls_drawn)
        # if the ball that was drawn is in the expectedBalls,
        # lower its value by 1
        for ball in drawnBalls:
            if ball in expectedBalls:
                expectedBalls[ball] -= 1

        # If all the expected_balls were drawn,
        # the experiment was successful
        if all(a <= 0 for a in expectedBalls.values()):
            matches += 1

    return matches / num_experiments