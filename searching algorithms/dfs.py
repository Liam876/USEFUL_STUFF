from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack



def dfs (maze,start,goal,pred = {}):
    offs =   {
    "down": (1, 0),
    "right": (0, 1),
    "up": (-1, 0),
    
    "left": (0, -1),
}
    res_pred = dfs1(maze,start,goal,offs,{},[False])
    print(res_pred)
    return get_path(res_pred,start,goal)



def dfs1(maze, start, goal, offs, pred = {}, flag = [False]):
    
    
    if pred == {}:
        pred[start] = None
    cc = start
    
    
    for key,value in offs.items():
        #print(value,cc)
        #print(key)
        newpos= tuple(cc[i] + value[i] for i in range(len(cc)))
        
        # Stop condition:
        
        if cc == goal:
            flag[0] = True
            return pred
        
        #print(is_legal_pos(maze, newpos), "\n", newpos not in pred )
        
        # Check each direction
        
        if is_legal_pos(maze, newpos) and newpos not in pred :         
            pred[newpos] = cc
            #print("\n" , key, "\n")
            dfs1(maze,newpos, goal, offs, pred, flag)
            
            # Check if desired goal reached when coming back
            
            if flag[0] == True:
                return pred
             
    
    


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test 2
    maze = read_maze(r"C:\Users\Admin\pracExc\Exercise Files\Ex_Files_Python_Data_Structures\Exercise Files\05_02_end\mazes/mini_maze_dfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 0)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0)]

    # Test 3
    maze = read_maze(r"C:\Users\Admin\pracExc\Exercise Files\Ex_Files_Python_Data_Structures\Exercise Files\05_02_end\mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (0,2 )
    result = dfs(maze, start_pos, goal_pos)
    print(result)
    #assert result is None
