"""The Bowling Game Scorer."""

# Standard Library

# 3rd Party Library

# Project Library


# -----------------------------------------------------------------------------
class BowlingFrame:
    """Keeping the record of each bowling frame."""

    def __init__(self, max_roll=2):
        """Construct a frame."""
        self.pins = [0] * max_roll
        self.max_roll = max_roll
        self.next_roll = 0

    def roll(self, pins: int):
        """Roll the ball swipe pins"""
        if self.next_roll < self.max_roll:
            self.pins[self.next_roll] = pins
            self.next_roll += 1

    def score(self):
        """Score of each frame."""
        return sum(self.pins)

    def is_spare(self):
        """Check if the current frame is a spare."""
        return self.score() == 10 and self.pins[0] != 10

    def is_strike(self):
        """Check if the current frame is a strike."""
        return self.pins[0] == 10


class BowlingFrame10(BowlingFrame):
    """Keeping the record of the 10th bowling frame."""

    def __init__(self):
        """Construct a frame."""
        super().__init__(3)


class BowlingGame:
    """The Bowling Game."""

    GAME_COMPLETE = -1

    def __init__(self):
        """Construct a BowlingGame object."""
        self.frames = []
        for _ in range(9):
            self.frames.append(BowlingFrame())

        self.frames.append(BowlingFrame10())
        self.cur_frame = 0  # current frame index
        self.cur_roll = 1  # current roll in frame

    def roll(self, num_of_pins: int):
        """Roll a bowling ball.

        Args:
            num_of_pins: The number of knocked-down pins

        Returns:
            None

        """
        frame = self.frames[self.cur_frame]
        frame.roll(num_of_pins)

        if self.cur_frame < 9:
            if frame.is_strike() or frame.next_roll == 2:
                self.cur_frame += 1
                self.cur_roll = 1
            else:
                self.cur_roll += 1
        elif self.cur_frame == 9:
            if frame.is_strike() and frame.next_roll == 1:
                self.cur_roll += 1
            elif frame.is_spare() or frame.next_roll == 2:
                self.cur_roll += 1
            else:
                self.cur_roll += 1
                self.cur_frame = self.GAME_COMPLETE

    def score(self):
        """Get the current score.

        Returns:
            The current score.

        """
        total = 0

        for index in range(len(self.frames)):
            frame = self.frames[index]
            total += frame.score()

            # Handling spare bonus
            if frame.is_spare() and index < 9:
                total += self.frames[index + 1].pins[0]

            # Handling strike bonus
            if frame.is_strike():
                if index < 9:
                    next_frame = self.frames[index + 1]
                    if next_frame.next_roll == 1:
                        total += next_frame.score() + self.frames[index + 2].pins[0]
                    else:
                        total += next_frame.score()

        return total
