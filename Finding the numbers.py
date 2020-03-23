#https://practice.geeksforgeeks.org/problems/finding-the-numbers/0
# XOR based solution https://www.geeksforgeeks.org/find-the-two-numbers-with-odd-occurences-in-an-unsorted-array/


T = int(input())
for t in range(T):
    N = int(input())
    arr = [int(x) for x in input().split()]
    # print(arr)
    
    set_ =set()
    
    for i in range(len(arr)):
        # print(arr[i])
        if arr[i] in set_:
            set_.remove(arr[i])
            # pass
        else:
            set_.add(arr[i])
            # pass
    
    arr_ = [x for x in arr if x in set_ ]
    arr_ = sorted(set(arr_))
    print(*arr_,sep=" ")
