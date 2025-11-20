'''
Array Triplets with Pythagorean Property
Given an integer array of length n, return a result array of length n-2, where result[i] = 1 if:

array[i]^2 + array[i+1]^2 = array[i+2]^2,
array[i+1]^2 + array[i+2]^2 = array[i]^2, and
array[i]^2 + array[i+2]^2 = array[i+1]^2.
Otherwise, result[i] = 0.
'''

def arrTriplets(arr, n): 
    res = [0] * (n-2)
    for i in range(n-2): 

        sum1 = arr[i]**2 + arr[i+1]**2
        sum2 = arr[i+1]**2 + arr[i+2]**2
        sum3 = arr[i]**2 + arr[i+2]**2

        if sum1 == arr[i+2]**2 and sum2 == arr[i]**2 and sum3 == arr[i+1]**2: 
            res[i] = 1
        else: 
            res[i] = 0
    return res
            


arr = [0, 0, 0, 0]
n = len(arr)
print(arrTriplets(arr, n))  # Expected: [1, 1]

arr = [3, 4, 5, 6, 8, 10]
n = len(arr)
print(arrTriplets(arr, n))  # Expected: [0, 0, 0, 0]

arr = [0, 0, 0, 5, 0]
n = len(arr)
print(arrTriplets(arr, n))  # Expected: [1, 0, 0]