import random

from numpy import maximum
student_id = input('Enter your student id: ')
print(student_id)
Upper_threshold = -1000
Lower_threshold = 1000
shuffle_count = 8
shuffle_list = []
win_time = 0


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


def alpha_beta_pruning(node_level, tree_index, whatPlayer, values, alpha, beta):
    if node_level == 3:
        return values[tree_index]
    
    if whatPlayer:
        best_node_value = Upper_threshold

        for iter in range(0, 2):
            temp_val = alpha_beta_pruning(node_level + 1, tree_index * 2 + iter, False, values, alpha, beta)
            best_node_value = max(best_node_value, temp_val)
            alpha = max(alpha, best_node_value)

            if beta <= alpha:
                break
        
        return best_node_value

    else:
        best_node_value = Lower_threshold
        for iter in range(0, 2):
            temp_val = alpha_beta_pruning(node_level + 1, tree_index * 2 + iter, True, values, alpha, beta)

            best_node_value = min(best_node_value, temp_val)
            beta = min(beta, best_node_value)

            if beta <= alpha:
                break
        return best_node_value


if __name__ == '__main__':
    min_point, max_point, point_to_win = min_and_max_point(student_id)
    # print(min_point, max_point, point_to_win)
    random_list = generate_list(min_point, max_point)
    # print(random_list)


    result = alpha_beta_pruning(0, 0, True, random_list, Upper_threshold, Lower_threshold)
    
    print(f'Generated 8 random points between the minimum and maximum point \nlimits: {random_list} \nTotal points to win: {point_to_win} \nAchieved point by applying alpha-beta pruning = {result}')

    
    if result >= point_to_win:
        print('The winner is Optimus Prime')
    else:
        print('The winner is Megratron')

    

    for itr in range(shuffle_count):
        random_list = generate_list(min_point, max_point)
        achieved_point = alpha_beta_pruning(0, 0, True, random_list, Upper_threshold, Lower_threshold)
        shuffle_list.append(achieved_point)
        
        maximum_value = max(shuffle_list)

    for points in shuffle_list:
        if points >= point_to_win:
            win_time += 1

    print(f'List of all points values from each shuffle: {shuffle_list} \nThe maximum value of all shuffles: {maximum_value} \nWon {win_time} times out of {shuffle_count} number of shuffles')




