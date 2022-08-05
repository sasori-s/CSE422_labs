def DFS(matrix,m_row,m_column,visited_list,max_counter):
    visited_list[m_row][m_column]=1
    steps=[[0,1],[1,0],[-1,1],[1,-1],[1,1],[-1,0],[0,-1],[-1,-1]]
    
    for s in range (len(steps)):
        if (Find_Affected_Region(matrix,m_row+steps[s][0],m_column+steps[s][1],visited_list)==True):
            max_counter[0] += 1
            DFS(matrix,m_row+steps[s][0],m_column+steps[s][1],visited_list,max_counter)



def Find_Affected_Region(matrix,m_row,m_column,visited_list):
    if ((m_row<len(matrix)) and (m_row>=0)  
    and (m_column<len(matrix[0])) and (m_column>=0) 
    and (matrix[m_row][m_column] and not visited_list[m_row][m_column])):
      return True

def Largest_Affected_Region(matrix):
    visited_list=[]
    r= 0
    affected_region_list=[]

    for i in range(len(matrix)):
      visited_list.append([0]*len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] and not visited_list[i][j]):
                max_counter = [1]
                DFS(matrix,i,j,visited_list,max_counter)
                max_affected = max(r, max_counter[0])
                affected_region_list.append(max_affected)
    return affected_region_list 



input_files=[r"D:\VS code\GeekForGeeks\Miscellenous\422Lab1.txt"]

for k in range(len(input_files)):
  matrix=[]
  with open(input_files[k]) as f:
    lines=f.readlines()
  for line in lines:
    matrix.append(line.split())

  for r in matrix:
    for c in range(len(r)):
      if r[c]=='Y':
        r[c]=1      
      else:
        r[c]=0
  print("List of affected regions:",Largest_Affected_Region(matrix))
  X=Largest_Affected_Region(matrix)
  output=max(X)
  print("Maximum affected region: ",output)