# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    if right == 0:  # There is no element in the input array
        return -1
    elif right == 1:  # There is only one element in the input array
        if x == a[0]:
            return 0
        else:
            return -1
                
    middle = (left + right)//2
    #print(left, right, middle)         
    #print(middle)         
    if x == a[middle]:
        #print("A: ",middle)
        return middle
    elif x > a[middle]:
        #print("B-1: ",middle)
        m = binary_search(a[middle+1:],x)
        #print("B-2: ",m)
        if m >= 0:
            return  m + middle + 1
        return -1
    else:
        #print("C-1: ",middle)
        m = binary_search(a[0:middle],x)
        #print("C-2: ",m)
        if m >= 0:
            return  m
        return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1] # number of data to be searched.
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
   