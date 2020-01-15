# Grid World Path Finder
This is a side-by-side visualization of the BFS and A-STAR algorithms.

This shows that by having a model of the search graph that gives an heuristic function, makes the A* algorithm explore the graph much more efficiently without losing the optimallity of the found path.

In this problem the heuristic function used is the L1 distance, also called the Mannhatan distance, between the tile you are in to the end tile. This is the distance between the current tile and the end using the movements LEFT,RIGHT,DOWN,UP in a underconstrained enviroment where we can move to a block tile. Since the exploration graph in the original graph is contained in the exploration graph of the underconstrained one we have that that the L1 distance is less or equal to the actual distance to the end in the original problem.

![Program visualization](img/a_star.png)

# Running the program
To use it, run the main file with
```
python main.py
```
Make sure to have pygame installed, if you don't get it with

```
pip install pygame
```
# Commands
__'r' key__ -  generates a new gridworld
