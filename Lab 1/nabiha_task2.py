def BFS(discovered,xcity,Queue,time):
  if len(Queue)==0:
    return discovered,xcity,Queue,time
  else:
    start_node=Queue.pop(0)
  counter=0
  row=start_node[0]
  column=start_node[1]
  valid_attack=[[0,1],[1,0],[0,-1],[-1,0]]
  for i in valid_attack:
    n_r=row+i[0]
    n_c=column+i[1]
    if(n_r>=0 and n_c>=0 and n_r<len(xcity) and n_c<len(xcity[0])):
      if not discovered[n_r][n_c] and xcity[n_r][n_c]==1:
        discovered[n_r][n_c]=True
        xcity[n_r][n_c]=0
        counter+=1
        Queue.append([n_r,n_c])

  if counter>0:
    discovered,xcity,Queue,time=BFS(discovered,xcity,Queue,time+1)  
  else:
    discovered,xcity,Queue,time=BFS(discovered,xcity,Queue,time)
  return discovered,xcity,Queue,time


input_files=[r"D:\VS code\GeekForGeeks\CSE422\Lab 1\task2_input.txt"]
for k in range(len(input_files)):
  with open(input_files[k]) as f:
    xcity=[]
    row= f.readline()
    column=f.readline()
    lines=f.readlines()

    for line in lines:
      xcity.append(line.split())
  alien=[]

  discovered=[]
  for i in range(int(row)):
    discovered.append([])
    for j in range(int(column)):
      discovered[i].append(False)

      if ("A" in xcity[i][j]):
        xcity[i][j]=0
        alien.append([i,j])
      elif ("H" in xcity[i][j]):
        xcity[i][j]=1
      else: 
        xcity[i][j]=2


  max_time=0
  Queue=[]
  for i in alien:
    Queue.append(i)
    discovered,xcity,Queue,time=BFS(discovered,xcity,Queue,0)
    max_time=max(max_time,time)
  human=0
  for i in range(int(row)): 
    for j in range(int(column)):
      
      if xcity[i][j]==1:
        human+=1
  print("For File input",k+1,":")
  if human==0:
    print(f'Time: {max_time} min')
    print(f'No one survived ')
  else:
    print(f'Time: {max_time} min')
    print(f'{human} survived')