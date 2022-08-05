from collections import deque


row_traverse = [1, 0, -1, 0]
col_traverse = [0, 1, 0, -1]

def readFile():
    count = 1
    alien_human = []
    with open(r"D:\VS code\GeekForGeeks\CSE422\Lab 1\task2_input.txt") as fp:
        for line in fp:
            if count == 1:
                count = 2
                row = int(line)
            
            elif count == 2:
                count = 0
                col = int(line)
            
            else:
                alien = [items.strip() for items in line.split()]
                alien_human.append(alien)
    
    return alien_human, row, col

def willEat(n_row, n_col, visited, alien_human_list):
    return (n_row >= 0 and n_row < len(visited)) and (n_col >= 0 and n_col < len(visited[0])) and not visited[n_row][n_col] and alien_human_list[n_row][n_col] == 'H'


def BFS(alien_human_list, i, j, visited):
    q = deque()
    q.append((i, j))

    visited[i][j] = True
    sub_time_list = []

    while q:
       x, y = q.popleft()
       
       for r in range(len(row_traverse)):
        if willEat(x + row_traverse[r], y + col_traverse[r], visited, alien_human_list):
            alien_human_list[x + row_traverse[r]][ y + col_traverse[r]] = 'A'
            visited[x + row_traverse[r]][ y + col_traverse[r]] = True
            q.append((x + row_traverse[r], y + col_traverse[r]))
            
            if (x, y) not in sub_time_list:
                sub_time_list.append((x, y))
            
    return len(sub_time_list)   




def checkAlien(alien_human_list, row, col):
    if not alien_human_list or not(len(alien_human_list)):
        return 0

    visited = [[False for i in range(col)] for j in range(row)]
    
    time = 0
    islands = 0
    for i in range(row):
        for j in range(col):
            if alien_human_list[i][j] == 'A' and not visited[i][j]:
                sub_time = BFS(alien_human_list, i, j, visited)

                if sub_time > time:
                    time = sub_time
    return f'{time} minutes'


def countHuman(alien_human_list, row, col):
    human_count = 0
    for i in range(row):
        for j in range(col):
            if alien_human_list[i][j] == 'H':
                human_count += 1

    return f'{human_count} survived' if not human_count == 0 else f'No one survived'



if __name__ == '__main__':
    alien_human_list, row, col = readFile()
    # print(alien_human_list)
    # print(row, col)
    print('Time ', checkAlien(alien_human_list, row, col))

    print(countHuman(alien_human_list, row, col))