import random

def majority_element(arr,n):
    d={}
    for i in range(n):
        count = 0
        for num in arr:
            if arr[i]==num:
                count += 1
        if arr[i] not in d:
            d[arr[i]]=count
    maj=0
    for num,count in d.items():
        if count>maj:
            maj=count
            maj_ele=num
    return maj_ele
        
try:
    A = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    N = len(A)
    if N == 0:
        N = int(input("Enter the size of the array (1 <= N <= 10^6): "))
        if N < 1 or N > 10**6:
            raise ValueError("Invalid array size")
        A = [random.randint(1, 10**9) for _ in range(N)]
    if N < 1 or N > 10**6:
        raise ValueError("Invalid array size")
    
    majority = majority_element(A,N)

    print("Input Array:", A)
    print("Majority Element:", majority)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An error occurred:", e)
