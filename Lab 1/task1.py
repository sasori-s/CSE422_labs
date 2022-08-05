from collections import deque

row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]

def readFile():
    corona_list = []
    with open(r"D:\VS code\GeekForGeeks\Miscellenous\422Lab1.txt") as textfile:
        for line in textfile:
            corona = [item.strip() for item in line.split()]
            corona_list.append(corona)

    # print(corona_list)
    return corona_list   

def infection(corona_list, x, y, chekced):
    return (x >= 0 and x < len(chekced)) and (y >= 0 and y < len(chekced)) and corona_list[x][y] == 'Y' and not chekced[x][y] 


def BFS(corona_list, chekced, i, j, biggest_area):
    queues = deque()
    queues.append((i, j))
    most_patient = 1

    chekced[i][j] = True

    while queues:
        x, y = queues.popleft()

        for k in range(len(row)):
            if infection(corona_list, x + row[k], y + col[k], chekced):
                chekced[x + row[k]][y + col[k]] = True
                queues.append((x + row[k], y + col[k]))
                most_patient += 1

    if most_patient > biggest_area:
        return most_patient
    else:
        return biggest_area


def countArea(corona_list):
    if not corona_list or not len(corona_list):
        return 0
    
    M, N = (len(corona_list), len(corona_list[0]))
    chekced = [[False for x in range(N)] for y in range(M)]

    biggest_area = 0
    # islands = 0
    for i in range(M):
        for j in range(N):
            if corona_list[i][j] == 'Y' and not chekced[i][j]:
                biggest_area = BFS(corona_list, chekced, i, j, biggest_area)
                # islands += 1
    return biggest_area

if __name__ == '__main__':
 
    corona_list = readFile()
    print('Maximum infection count is', countArea(corona_list))
    