# Two Bucket

# Instructions
# Given two buckets of different size and which bucket to fill first, determine how many actions are required to measure an exact number of liters by strategically transferring fluid between the buckets.

# There are some rules that your solution must follow:

# You can only do one action at a time.
# There are only 3 possible actions:
# Pouring one bucket into the other bucket until either:
#   a) the first bucket is empty
#   b) the second bucket is full
# Emptying a bucket and doing nothing to the other.
# Filling a bucket and doing nothing to the other.

# After an action, you may not arrive at a state where the initial
# starting bucket is empty and the other bucket is full.
# Your program will take as input:

# the size of bucket one
# the size of bucket two
# the desired number of liters to reach
# which bucket to fill first, either bucket one or bucket two

# Your program should determine:

# the total number of actions it should take to reach the desired
# number of liters, including the first fill of the starting bucket
# which bucket should end up with the desired number of liters -
# either bucket one or bucket two how many liters are left in the other bucket

# Note: any time a change is made to either or
# both buckets counts as one (1) action.

# Example: Bucket one can hold up to 7 liters, and bucket two can hold up to 11 liters.
# Let's say at a given step, bucket one is holding 7 liters and bucket two is holding 8 liters (7,8).
# If you empty bucket one and make no change to bucket two,
# leaving you with 0 liters and 8 liters respectively (0,8), that counts as one action.
# Instead, if you had poured from bucket one into bucket two until bucket two was full,
# resulting in 4 liters in bucket one and 11 liters in bucket two (4,11), that would also only count as one action.

# Another Example: Bucket one can hold 3 liters, and bucket two can hold up to 5 liters.
# You are told you must start with bucket one. So your first action is to fill bucket one.
# You choose to empty bucket one for your second action. For your third action,
# you may not fill bucket two, because this violates the third rule -
# - you may not end up in a state after any action where the starting bucket
# is empty and the other bucket is full.

# Written with <3 at Fullstack Academy by Lindsay Levine.

# Exception messages
# Sometimes it is necessary to raise an exception. When you do this,
# you should always include a meaningful error message to indicate what the source of the error is.
# This makes your code more readable and helps significantly with debugging.
# For situations where you know that the error source will be a certain type,
# you can choose to raise one of the built in error types,
# but should still include a meaningful message.

# This particular exercise requires that you use the raise statement to "throw" a ValueError.
# The tests will only pass if you both raise the exception and include a message with it.

# To raise a ValueError with a message, write the message as an argument to the exception type:

# raise ValueError("A meaningful error message here.")


from math import gcd


class TwoBucket:
    """
    Solve the classic two-bucket (water jug) problem.

    This class simulates two buckets with fixed capacities and allows
    filling, emptying, and pouring water between them in order to
    measure an exact target volume.
    """

    def __init__(
        self,
        bucket_one: int,
        bucket_two: int,
    ) -> None:
        """
        Initialize the TwoBucket problem with the given bucket capacities.

        Parameters
        ----------
        bucket_one : int
            Capacity of the first bucket.
        bucket_two : int
            Capacity of the second bucket.
        """
        self.bucket_one = 0
        self.bucket_two = 0
        self.capacity = (bucket_one, bucket_two)

    def pouring_into(self, receptor: str) -> tuple[int, int]:
        """
        Pour water from the opposite bucket into the specified receptor bucket.

        The transfer stops when either:
        - The source bucket becomes empty, or
        - The receptor bucket becomes full.

        Parameters
        ----------
        receptor : str
            The bucket that will receive water ("one" or "two").

        Returns
        -------
        tuple[int, int]
            The current amounts of water in bucket one and bucket two.
        """
        if receptor == "one":
            quantity = min(self.bucket_two, self.capacity[0] - self.bucket_one)
            self.bucket_one += quantity
            self.bucket_two -= quantity

        elif receptor == "two":
            quantity = min(self.bucket_one, self.capacity[1] - self.bucket_two)
            self.bucket_two += quantity
            self.bucket_one -= quantity

        return (self.bucket_one, self.bucket_two)

    def measure(
        self,
        goal: int,
        start_bucket: str,
    ) -> tuple[int, str, int]:
        """
        Determine the minimum number of moves required to measure the target volume.

        The algorithm follows a deterministic strategy:
        - Fill the starting bucket.
        - Repeatedly pour into the other bucket.
        - Refill the starting bucket when empty.
        - Empty the other bucket when full.

        Parameters
        ----------
        goal : int
            The desired amount of water to measure.
        start_bucket : str
            The bucket to fill first ("one" or "two").

        Returns
        -------
        tuple[int, str, int]
            A tuple containing:
            - The number of moves required.
            - The bucket that contains the goal volume ("one" or "two").
            - The amount of water in the other bucket.

        Raises
        ------
        ValueError
            If the goal is larger than both bucket capacities or
            cannot be measured (i.e., it is not a multiple of the
            greatest common divisor of the capacities).
        """
        # fill start bucket, tranfer to another, fill start bucket, transfer to another and empty another if full
        # first step
        if start_bucket == "one":
            self.bucket_one = self.capacity[0]
        elif start_bucket == "two":
            self.bucket_two = self.capacity[1]
        moves = 1

        if (
            goal > max(self.capacity)
            or goal % gcd(self.capacity[0], self.capacity[1]) != 0
        ):
            raise ValueError("Impossible")

        visited = set()

        while self.bucket_one != goal and self.bucket_two != goal:

            state = (self.bucket_one, self.bucket_two)
            if state in visited:
                raise ValueError("No solution found (loop detected)")
            visited.add(state)

            if start_bucket == "one":

                if self.bucket_one == 0:
                    self.bucket_one = self.capacity[0]

                elif self.bucket_two == self.capacity[1]:
                    self.bucket_two = 0

                else:
                    self.pouring_into("two")

            else:

                if self.bucket_two == 0:
                    self.bucket_two = self.capacity[1]

                elif self.bucket_one == self.capacity[0]:
                    self.bucket_one = 0

                else:
                    self.pouring_into("one")

            if (
                start_bucket == "one"
                and self.bucket_one == 0
                and self.bucket_two == self.capacity[1]
            ):
                raise ValueError("Invalid state: start bucket empty and other full")
            if (
                start_bucket == "two"
                and self.bucket_two == 0
                and self.bucket_one == self.capacity[0]
            ):
                raise ValueError("Invalid state: start bucket empty and other full")

            moves += 1

        goal_bucket: str = "one"
        another_bucket = 0

        if self.bucket_one == goal:
            goal_bucket = "one"
            another_bucket = self.bucket_two

        elif self.bucket_two == goal:
            goal_bucket = "two"
            another_bucket = self.bucket_one

        return (moves, goal_bucket, another_bucket)
