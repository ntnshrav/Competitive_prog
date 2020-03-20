#code
T = int(input())
for i in range(T):
    N,S  = [int(x) for x in (input().split())]
    arr = [int(x) for x in (input().split())]
    
    # print(N,S,arr)
    flag = False
    # trivial case 1 - cheack for the sum of enitre array 
    if(S == sum(arr)):
        print("{} {} ".format("1",N))
        flag = True
        # exit()
    
    # sliding window approach 
    for window_size in range(1,len(arr)+1):
        if(flag == False):
            for front in range(0,len(arr)-window_size+1,):
                # print(window_size,front)
                rear = front +window_size 
                print("checking: ",arr[front:rear])
                if(sum(arr[front:rear]) == S):
                    print("{} {}".format(front,rear))
                    flag = True 
        else:
            break
    if(flag == False):
        print("-1")
                
    ======================================================================
    #code
T = int(input())
for i in range(T):
    N,S  = [int(x) for x in (input().split())]
    arr = [int(x) for x in (input().split())]
    # print(N,S,arr)
    # trivial case 1 - cheack for the sum of enitre array 
    if(S == sum(arr)):
        print("{} {} ".format("1",N))
        # exit()
    # N - square approach 
    flag = False
    for front in range(len(arr)):
        if(flag == False):
            for rear in range(front+1,len(arr)+1):
                # if(front == 38):
                #     print(front,rear)
                #     print(arr[front:rear])
                if(sum(arr[front:rear]) ==  S):
                    print("{} {}".format(front+1,rear))
                    flag = True
                    # exit()
                else:
                    if(front +1 == len(arr)+1):
                        print("-1")
                        # exit()
        else:
            break
    if(flag == False):
        print("-1")
   ===========================================================
   optimal method
   
   #code
T = int(input())
for i in range(T):
    N,S  = [int(x) for x in (input().split())]
    arr = [int(x) for x in (input().split())]
    # print(N,S,arr)
    
    # optimul method 
    
    curr_sum  = arr[0]
    front = 1 
    start = 0 
    flag = False
    while(front  <= N):
        # print(curr_sum )
        
        while(curr_sum > S and start < front-1):
            curr_sum = curr_sum - arr[start]
            start = start + 1
            
        if(curr_sum == S):
            print("{} {}".format(start+1, front ))
            flag = True
            break 
            
        if(front < N):
            curr_sum += arr[front]
        
        front += 1
        
    if(flag == False):
         print("-1")
