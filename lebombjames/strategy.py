import random
from pprint import pprint

# previous_board = [[[0 for _ in range(5)] for _ in range(10)] for _ in range(10)]
# bombs = [[0 for _ in range(10)] for _ in range(10)]


# def update_bombs(board):
#     global previous_board
#     global bombs

#     for x in range(10):
#         for y in range(10):
#             if sum(board[x][y]) < sum(previous_board[x][y]):
#                 bombs[x][y] += 1

#     print("bombs:")
#     pprint(bombs)

#     previous_board = board


# def strategy(pid, board):
#     moves = []

#     update_bombs(board)

#     for move_number in range(3):
#         settlement_counts = [[0 for _ in range(10)] for _ in range(10)]

#         for x in range(10):
#             for y in range(10):
#                 total_settlements = sum(board[x][y])
#                 settlement_counts[x][y] = total_settlements

#         for move in moves:
#             settlement_counts[move[0]][move[1]] += 1

#         # print("current move number:", move_number)

#         danger_scores = danger_iteration(settlement_counts)
#         danger_scores = danger_iteration(danger_scores)

#         # print("settlement_counts:")
#         # pprint(settlement_counts)

#         # print("danger_scores:")
#         # pprint(danger_scores)

#         locations = []

#         for x, row in enumerate(danger_scores):
#             for y, score in enumerate(row):
#                 locations.append(((x, y), score))

#         random.shuffle(locations)

#         move = min(locations, key=lambda x: x[1])

#         # print(f"move number {move_number} has been decided: {move}")

#         moves.append(move[0])

#     # print("---------------------------------")

#     previous_board = board

#     return moves

BOARD_SIZE = 10
NUM_PLAYERS = 5
REAL_GAME_START = 900
NUM_MOVES = 3

iteration = 0
previous_board = [
    [[0 for _ in range(NUM_PLAYERS)] for _ in range(BOARD_SIZE)]
    for _ in range(BOARD_SIZE)
]
bomb_counts = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def strategy(pid, board):
    global iteration
    global previous_board
    global bomb_counts

    # update bomb counts
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if sum(board[x][y]) < sum(previous_board[x][y]):
                bomb_counts[x][y] += 1

    iteration += 1
    previous_board = board

    moves = []

    for move_number in range(NUM_MOVES):
        # print("current move number:", move_number)

        settlement_counts = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                settlement_counts[x][y] = sum(board[x][y])

        # add own previous moves to settlement counts
        for move in moves:
            settlement_counts[move[0]][move[1]] += 1

        danger_scores = danger_iteration(settlement_counts)
        danger_scores = danger_iteration(danger_scores)

        # add bomb counts to danger scores
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                danger_scores[x][y] += bomb_counts[x][y]

        # print("settlement_counts:")
        # pprint(settlement_counts)

        # print("danger_scores:")
        if iteration % 1000 == 0:
            pprint(danger_scores)

        locations = []
        for x in range(BOARD_SIZE):
            for y, score in enumerate(danger_scores[x]):
                locations.append(((x, y), score))

        random.shuffle(locations)

        move = min(locations, key=lambda x: x[1])

        # print(f"move number {move_number} has been decided: {move}")

        moves.append(move[0])

    # print("---------------------------------")

    return moves


def danger_iteration(counts):
    danger_scores = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            danger_score = counts[x][y]
            for nx, ny in get_neighbors(x, y):
                danger_score += counts[nx][ny]
            danger_scores[x][y] = danger_score
    return danger_scores


def get_neighbors(x, y):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < 9:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < 9:
        neighbors.append((x, y + 1))
    return neighbors


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
