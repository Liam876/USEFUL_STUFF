from helpers import get_path, offsets, is_legal_pos, read_maze

from priority_queue import PriorityQueue


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def fval1 (cur,start,goal):
    g_val = heuristic(cur, start)
    h_val = heuristic(cur, goal)
    
    return g_val + h_val


def a_star(maze, start, goal):
    
    def fval (cur):
        return fval1(cur,start,goal)
    
    
    prq = PriorityQueue()
    prq.put(start,fval(start))
    pred =  {start : None}
    
    
    
    while not prq.is_empty():
        cc = prq.get()
        if cc == goal:
            return get_path(pred, start, goal)
        for key,value in offsets.items():
            newpos= tuple(cc[i] + value[i] for i in range(len(cc)))
            if is_legal_pos(maze, newpos) and newpos not in pred : 
                prq.put(newpos, fval(newpos))
                pred[newpos] = cc
            
    

if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
