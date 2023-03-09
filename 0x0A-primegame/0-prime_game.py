def is_winner(x, nums):
    """
    Given a set of consecutive integers starting from 1 up to and including n,
    they take turns choosing a prime number from the set and removing that number
    and its multiples from the set. The player that cannot make a move loses the game.
    This function determines the winner of x rounds of the game, where n may be different
    for each round. Assuming Maria always goes first and both players play optimally.

    Args:
    x (int): the number of rounds to play
    nums (list[int]): an array of n values, where n is the highest integer value
                      in the set of consecutive integers for each round

    Returns:
    str: the name of the player that won the most rounds
    None: if the winner cannot be determined
    """
    def sieve(n):
        """
        Helper function that generates all prime numbers up to n using the Sieve of Eratosthenes algorithm.

        Args:
        n (int): the upper limit of the range of numbers to check for primes

        Returns:
        list[int]: a list of all prime numbers up to n
        """
        # Initialize a boolean array to mark prime and composite numbers
        primes = [True] * (n+1)
        primes[0] = primes[1] = False

        # Iterate over all numbers up to sqrt(n), marking all multiples of primes as composite
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False

        # Return a list of all prime numbers in the range [0, n]
        return [i for i in range(n+1) if primes[i]]

    def play(n):
        """
        Helper function that simulates a single round of the game for a given n.

        Args:
        n (int): the upper limit of the range of integers to play with

        Returns:
        int: the number of the winning player (1 or 2)
        """
        # Generate a list of all prime numbers up to n
        primes = sieve(n)

        # Initialize the player to start with and continue playing until the game is over
        player = 1
        while True:
            # Get a list of all possible moves (i.e., primes that are still in the set of available numbers)
            possible_moves = [p for p in primes if p in nums]

            # If there are no possible moves left, the current player loses
            if not possible_moves:
                return player

            # Choose the largest possible move and remove it and its multiples from the set of available numbers
            move = possible_moves[-1]
            nums.difference_update(set(range(move, n+1, move)))

            # Switch to the other player
            player = 3 - player

    # Initialize counters for the number of rounds each player wins
    maria_wins = 0
    ben_wins = 0

    # Iterate over all values of n in the nums array and determine the winner of each round
    for n in nums:
        winner = play(n)
        if winner == 1:
            maria_wins += 1
        elif winner == 2:
            ben_wins += 1

    # Determine the overall winner of all rounds played
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
