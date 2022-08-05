import random

inp_std_id = int(input('Enter the id: '))



MXMUM, MINIM = 1000, -1000
def mnmx(dpt, nIndx, maxiP,
            valz, alphA, betA):
  
   
    if dpt == 3:
        return valz[nIndx]
 
    if maxiP:
      
        bst = MINIM
 
        
        for i in range(0, 2):
             
            val = mnmx(dpt + 1, nIndx * 2 + i,
                          False, valz, alphA, betA)
            bst = max(bst, val)
            alphA = max(alphA, bst)
 
            
            if betA <= alphA:
                break
          
        return bst
      
    else:
        bst = MXMUM
 
        
        for i in range(0, 2):
          
            val = mnmx(dpt + 1, nIndx * 2 + i,
                            True, valz, alphA, betA)
            bst = min(bst, val)
            betA = min(betA, bst)
 
           
            if betA <= alphA:
                break
          
        return bst
      

if __name__ == "__main__":
  
    valz = [1, 9, 6, 5, 1, 4, 0, -1] 
    print("The ideal optimized number is :", mnmx(0, 0, True, valz, MINIM, MXMUM))
