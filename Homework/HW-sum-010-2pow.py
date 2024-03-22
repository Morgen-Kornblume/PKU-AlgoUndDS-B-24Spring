def calc(x : int):
    
    for i in range(14, -1, -1):
        if(x == 2 ** i):
            if(i == 1): print("2",end="")
            elif(i == 0): print("2(0)",end="")
            else:
                print("2(",end="")
                calc(i)
                print(")",end="")
            break
        elif(x > 2 ** i):
            if(i == 1): 
                print("2+",end="")
                calc(x - 2)
            else:
                print("2(",end="")
                calc(i)
                print(")+",end="")
                calc(x - 2 ** i)
            break 

n = int(input())
calc(n)