import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue

def solve_maze(maze):
    start = (0, 0)
    end = (7, 7)
    path = a_star(maze, start, end)
    return path

def a_star(maze, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    rows, cols = len(maze), len(maze[0])
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    steps = []

    while not open_set.empty():
        _, current = open_set.get()
        steps.append(current)  # Store current step for animation
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, steps

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            tentative_g_score = g_score[current] + 1
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == 0:
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    open_set.put((f_score[neighbor], neighbor))

    return [], steps

def create_maze_image(maze, steps=None, path=None):
    maze_array = np.array(maze)
    plt.figure(figsize=(6, 6))
    plt.imshow(maze_array, cmap='gray')

    # Mark the start and end
    plt.text(0, 0, 'S', color='green', ha='center', va='center', fontsize=12, fontweight='bold')
    plt.text(len(maze[0])-1, len(maze)-1, 'E', color='red', ha='center', va='center', fontsize=12, fontweight='bold')

    if steps:
        for step in steps:
            plt.text(step[1], step[0], 'O', color='yellow', ha='center', va='center')

    if path:
        for step in path:
            plt.text(step[1], step[0], 'P', color='blue', ha='center', va='center')

    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.grid(which='both')
    plt.gca().invert_yaxis()
    plt.gca().set_xticks(np.arange(-.5, len(maze[0]), 1), minor=True)
    plt.gca().set_yticks(np.arange(-.5, len(maze), 1), minor=True)
    plt.gca().grid(which='minor', color='black', linestyle='-', linewidth=2)

    plt.show()

    # Save the image
    plt.savefig('maze.png')
    plt.close()

    return 'maze.png'
