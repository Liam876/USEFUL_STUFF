from helpers import get_path, offsets, is_legal_pos, read_maze
from queue_ll import Queue


def bfs(maze, start, goal):
    q = Queue()
    q.enqueue(start)
    pred = {start : None}
    
    while (not q.is_empty()):
        cc = q.dequeue()
        if cc == goal:
            return get_path(pred, start, goal)
        else:
            for key,value in offsets.items():
                newpos= tuple(cc[i] + value[i] for i in range(len(cc)))
                if is_legal_pos(maze, newpos) and newpos not in pred : 
                    q.enqueue(newpos)
                    pred[newpos] = cc
                    

                    
                    
                    
                    
                    

if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    print(result)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze(r"C:\Users\Admin\pracExc\Exercise Files\Ex_Files_Python_Data_Structures\Exercise Files\05_02_end\mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze(r"C:\Users\Admin\pracExc\Exercise Files\Ex_Files_Python_Data_Structures\Exercise Files\05_02_end\mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
