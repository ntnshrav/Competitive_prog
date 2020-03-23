#https://practice.geeksforgeeks.org/problems/maximum-index/0
T = int(input())
for t in range(T):
    N = int(input())
    arr = [int(x) for x in input().split()]
    
    max_ = 0
    i  = 0 
    j = N-1
    while (i<j):
        # print(arr[i],arr[j])
        if(arr[i]<=arr[j] and (j-i)>max_):
            max_ = j-i
            break 
        else:
            if(arr[j-1]<=arr[i] and (j-1)!=i):
                # print(arr[i],arr[j-1])
                max_ = j-1-i
            else:
                if(arr[j]>=arr[i+1] and j!=(i+1)):
                    # print(arr[i+1],arr[j])
                    max_ = j-i-1
        i +=1
        j -=1
    print(max_)
