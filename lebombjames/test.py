import random

from grid import Grid


def strategy(pid, player_boards):
    board = [[[0 for _ in range(2)] for _ in range(10)] for _ in range(10)]
    for player_board in player_boards:
        for i, row in enumerate(player_board):
            for j, item in enumerate(row):
                board[i][j][0] += item

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            neighbors = [board[x][y][0] for x, y in get_neighbors(i, j)]
            for neighbor in neighbors:
                board[i][j][1] += neighbor

    print(board)


def get_neighbors(i, j):
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j))
    if i < 9:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < 9:
        neighbors.append((i, j + 1))
    return neighbors


def random_strategy(pid, board):
    return [
        (random.randint(0, 9), random.randint(0, 9)),
        (random.randint(0, 9), random.randint(0, 9)),
        (random.randint(0, 9), random.randint(0, 9)),
    ]


players = [
    strategy,
    random_strategy,
    random_strategy,
    random_strategy,
    random_strategy,
]

grid = Grid()
state = grid.state()

grid.step(
    [
        [(0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0)],
    ]
)

for i, player in enumerate(players):
    output = player(i, state)
    # grid.step(output)


# output = strategy(0, grid.state())
