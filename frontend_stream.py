import streamlit as st
import numpy as np
import time
from PIL import Image
import maze_solver

def load_image(path):
    image = Image.open(path)
    return image


maze = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 0]
]

st.title("Maze Solver")
st.write("This app uses the A* algorithm to solve the maze.")

if st.button("Solve"):
    st.write("Solving the maze...")
    path, steps = maze_solver.solve_maze(maze)
    
   
    image_placeholder = st.empty()

    for i in range(len(steps)):
        maze_solver.create_maze_image(maze, steps=steps[:i+1], path=None)
        image = load_image('maze.png')
        image_placeholder.image(image, caption=f'Step {i+1}', use_column_width=True)
        time.sleep(0.5)  # Adjust the speed of animation here

    maze_solver.create_maze_image(maze, steps=steps, path=path)
    image = load_image('maze.png')
    image_placeholder.image(image, caption='Final Path', use_column_width=True)

st.write("Maze solving complete.")
