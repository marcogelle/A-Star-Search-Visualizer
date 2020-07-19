# A* Search Visualizer
Required software: Python 3

To run the program: run GUI.py, located in the 'search visualizer' directory

This project aims to visualize how the A* pathfinding algorithm runs and show the effects of different heuristics. The user is able to choose a starting position on the grid, a desired goal position, draw obstacles, choose a heuristic, and run the A* search algorithm to find a path from the start to the goal. In the current version, the user has four options for the heuristic:

1. Manhattan distance: The Manhattan distance performs comparatively well. It is consistent, ensuring optimality/finding the shortest path. Compared to the other consistent heuristics, it checks the least amount of states/grid positions, making it the most efficient.

2. Euclidean distance: Another consistent heuristic. However, it checks more unnecessary grid positions than the Manhattan heuristic, since the Manhattan distance is always greater than or equal to the Euclidean distance.

3. Trivial heuristic: Always returns 0. The A* search algorithm essentially turns into a Uniform-Cost Search. While it is less computationally efficient, this still guarantees the finding the shortest path.

4. Double Manhattan: An inadmissible heuristic that returns double the Manhattan distance. This causes the A* search to degrade into a Greedy Breadth-First-Search algorithm. Less positions are checked, but finding the shortest path is not guaranteed.


Controls:


Make/remove walls: click and drag on the grid

Choose starting position: enter the x,y coordinates and press the "Start" button

Choose goal position: enter the x,y coordinates and press the "Destination" button

Run pathfinding: choose the heuristic from the dropdown menu and press "Start Search"

Clear the grid: press "Clear"
