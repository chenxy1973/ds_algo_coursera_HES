# Uses python3
import sys

# First trial. But refused by grader due to time-exceeding-the-limit.
def binary_search_0(a, x):
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
        m = binary_search_0(a[middle+1:],x)
        #print("B-2: ",m)
        if m >= 0:
            return  m + middle + 1
        return -1
    else:
        #print("C-1: ",middle)
        m = binary_search_0(a[0:middle],x)
        #print("C-2: ",m)
        if m >= 0:
            return  m
        return -1

# Even slower than binary_search_0! why?
def binary_search_1(a, x):
    left, right = 0, len(a)
    # write your code here
    #if right == 0:  # There is no element in the input array
    #    return -1
    #elif right == 1:  # There is only one element in the input array
    if right == 1:
        if x == a[0]:
            return 0
        else:
            return -1
    elif right == 2:
        if x == a[0]:
            return 0
        elif x == a[1]:
            return 1
        else:
            return -1
#    if x in a:
#        return a.index(x)
#    else:
#        return -1
    
    # len(a) >= 3           
    middle = (left + right)//2
    #print(left, right, middle)         
    #print(middle)         
    if x == a[middle]:
        #print("A: ",middle)
        return middle
    elif x > a[middle]:
        #print("B-1: ",middle)
        m = binary_search_1(a[middle+1:],x)
        #print("B-2: ",m)
        if m >= 0:
            return  m + middle + 1
        return -1
    else:
        #print("C-1: ",middle)
        m = binary_search_1(a[0:middle],x)
        #print("C-2: ",m)
        if m >= 0:
            return  m
        return -1

# NG!
def binary_search_2(a, x):
    left, right = 0, len(a)
    
    # write your code here

    # boundary-check     
    if x > a[-1] or x < a[0]:
        return -1
    
    # bottom-case
    if right == 0:  # There is no element in the input array
        return -1
    elif right == 1:  # There is only one element in the input array
        if x == a[0]:
            return 0
        else:
            return -1
     
#    elif right == 2:
#        if x == a[1]:
#            return 1
#        else:
#            return -1
                
    middle = int((left + right)/2)
    #print(left, right, middle)         
    #print(middle)         
    if x == a[middle]:
        #print("A: ",middle)
        return middle
    elif x > a[middle]:
    #if x >= a[middle]:
        #print("B-1: ",middle)
        m = binary_search_2(a[middle+1:right],x)
        #print("B-2: ",m)
        if m >= 0:
            return  m + middle + 1
        #return -1
    else:
        #print("C-1: ",middle)
        m = binary_search_2(a[0:middle],x)
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
   