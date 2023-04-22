import random
from pprint import pprint


def init_new_grid():
    return


bomb_counts = [[0 for _ in range(10)] for _ in range(10)]
previous_board = [[[0 for _ in range(5)] for _ in range(10)] for _ in range(10)]
iterations = 0


def update_bomb_counts(board):
    global bomb_counts
    for x in range(10):
        for y in range(10):
            if sum(board[x][y]) < sum(previous_board[x][y]):
                bomb_counts[x][y] += 1


def strategy(pid, board):
    global iterations

    # try to confuse people
    if iterations < 900:
        update_bomb_counts(board)
        iterations += 1
        return [
            (random.randint(0, 9), random.randint(0, 9)),
            (random.randint(0, 9), random.randint(0, 9)),
            (random.randint(0, 9), random.randint(0, 9)),
        ]

    # try to win
    # sample locations with least bombs
    locations = []
    for x, row in enumerate(bomb_counts):
        for y, count in enumerate(row):
            locations.append(((x, y), count))

    random.shuffle(locations)

    moves = [min(locations, key=lambda x: x[1])[0] for _ in range(3)]

    pprint(moves)

    return moves


def random_strategy(pid, board):
    return [
        (random.randint(0, 9), random.randint(0, 9)),
        (random.randint(0, 9), random.randint(0, 9)),
        (random.randint(0, 9), random.randint(0, 9)),
    ]


# Edit me!
def get_strategies():
    """
    Returns a list of strategy functions to use in a game.

    In the local tester, all of the strategies will be used as separate players in the game.
    Results will be printed out in the order of the list.

    In the official grader, only the first element of the list will be used as your strategy.
    """
    strategies = [
        strategy,
        random_strategy,
        random_strategy,
        random_strategy,
        random_strategy,
    ]

    return strategies
