import random


Lower_limit= -1000

Upper_limit= 1000

StudentId= input('Enter your student ID: ')

print(StudentId)

def NewList(leastValue, peakValue) :

    RandomValue = [ ]

    for m in range(8) :

        number= random.randint(leastValue,  peakValue)
        RandomValue.append(number)


    return RandomValue


def HighestPoint_AndLowestPoint(StudentId):
    LowestPoint=  StudentId[4]


    ForVictoryPointValue= StudentId[-1]  +  StudentId[-2]
  
    HighestPoint= int(ForVictoryPointValue)*  1.5

    return int(LowestPoint) , int(HighestPoint) , int(ForVictoryPointValue)




def AlphaBetaPruning(D, N_Index, maximizingPlayer, values, alpha, beta):

    if D==3 :
        return values[N_Index]

    if maximizingPlayer :
        AppropriateVal= Lower_limit


        for i in range(0,2) :

            NodePoint= AlphaBetaPruning(D+ 1 ,N_Index* 2+ i , False ,values,  alpha,  beta)
            AppropriateVal= max(AppropriateVal, NodePoint)
            alpha= max(alpha, AppropriateVal)

            if beta<= alpha :

                break
        
        return AppropriateVal

    
    else:
        
        AppropriateVal= Upper_limit
        
        for i in range(0,2) :
            NodePoint= AlphaBetaPruning(D + 1, N_Index * 2 + i, True, values, alpha, beta)

            AppropriateVal= min(AppropriateVal ,NodePoint)
            
            beta = min(beta ,AppropriateVal)

            if beta<= alpha :

                break
        
        return AppropriateVal


if __name__  == '__main__':
    
    shuffles = 7
    NewWinList = [ ]
    optimusWon = 0

    LowestPoint , HighestPoint ,ForVictoryPointValue= HighestPoint_AndLowestPoint(StudentId)
    RandomValues= NewList(LowestPoint, HighestPoint)
    Final= AlphaBetaPruning(0 ,0 ,True , RandomValues , Lower_limit , Upper_limit)

    print( f'Generated 8 random points between the minimum and maximum point \nlimits:  {RandomValues}  '
           f'\nTotal points to win:   {ForVictoryPointValue} '
           f'\nAchieved point by applying alpha-beta pruning= {Final} ' )

    
    if Final<  ForVictoryPointValue :
        print('The winner is Megatron')
    
    
    else:
        
        print('The winner is Optimus Prime')

    for shuff in range(shuffles):
        RandomValues = NewList(LowestPoint, HighestPoint)

        afterShufflePoint = AlphaBetaPruning(0, 0, True, RandomValues, Lower_limit, Upper_limit)

        NewWinList.append(afterShufflePoint)
        maximumPoint = max(NewWinList)

    for i in range(shuffles):
        if NewWinList[i] >= ForVictoryPointValue:
            optimusWon += 1
    
    print(f'List   of   all points  values  from each shuffle:   {NewWinList}   \nThe maximum value of all shuffles: {maximumPoint}   \nWon {optimusWon} times out of {shuffles}   number of  shuffles')





