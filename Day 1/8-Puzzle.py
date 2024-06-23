import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous

    def __lt__(self, other):
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())

    def manhattan_distance(self):
        distance = 0
        for i in range(9):
            if self.board[i] == 0:
                continue
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(self.board[i] - 1, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
        return distance

    def is_goal(self):
        return self.board == list(range(1, 9)) + [0]

    def neighbors(self):
        neighbors = []
        zero_index = self.board.index(0)
        x, y = divmod(zero_index, 3)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = self.board[:]
                new_index = nx * 3 + ny
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))

        return neighbors

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
        print()

def solve_8_puzzle(start_board):
    start_state = PuzzleState(start_board)
    if start_state.is_goal():
        return start_state

    pq = []
    heapq.heappush(pq, start_state)
    visited = set()

    while pq:
        current_state = heapq.heappop(pq)
        if current_state.is_goal():
            return current_state

        visited.add(tuple(current_state.board))

        for neighbor in current_state.neighbors():
            if tuple(neighbor.board) not in visited:
                heapq.heappush(pq, neighbor)

    return None

def print_solution(solution):
    steps = []
    state = solution
    while state:
        steps.append(state)
        state = state.previous
    steps.reverse()
    for step in steps:
        step.print_board()

# Example usage
start_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
solution = solve_8_puzzle(start_board)
if solution:
    print_solution(solution)
else:
    print("No solution found.")
