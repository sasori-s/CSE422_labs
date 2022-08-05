import random
student_id = input('Enter your student id: ')
print(student_id)
MIN = -1000
MAX = 1000


def min_and_max_point(student_id):
    min_point = student_id[4]
    # print(min_point)

    point_to_win = student_id[-1] + student_id[-2]
    # print(max_point)
    max_point = int(point_to_win) * 1.5

    return int(min_point), int(max_point), int(point_to_win)

def generate_list(min, max):
    random_list = []
    for i in range(0, 8):
        number = random.randint(min, max)
        random_list.append(number)
        
    return random_list


def minimax(deapth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if deapth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = MIN

        for i in range(0, 2):
            val = minimax(deapth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        
        return best

    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(deapth + 1, nodeIndex * 2 + i, True, values, alpha, beta)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best


if __name__ == '__main__':
    min_point, max_point, point_to_win = min_and_max_point(student_id)
    # print(min_point, max_point, point_to_win)
    random_list = generate_list(min_point, max_point)
    # print(random_list)


    result = minimax(0, 0, True, random_list, MIN, MAX)
    
    print(f'Generated 8 random points between the minimum and maximum point \nlimits: {random_list} \nTotal points to win: {point_to_win} \nAchieved point by applying alpha-beta pruning = {result}')

    
    if result >= point_to_win:
        print('The winner is Optimus Prime')
    else:
        print('The winner is Megratron')

    # print('THe optimal value is: ', minimax(0, 0, True, random_list, MIN, MAX))



