if __name__ == '__main__':
    
    n = int(input())
    arr = input().split()
        
    arr = [int(i) for i in arr]
    up=[-100,-99]




    for i in range(len(arr)):
        
        if arr[i] not in up:
            
            if arr[i] > up[1]:
                
                del up[0]
                up.append(arr[i])
            
            elif arr[i] < up[1] and arr[i] > up[0]:
                
                up[0] = arr[i]
        
    print(up[0])