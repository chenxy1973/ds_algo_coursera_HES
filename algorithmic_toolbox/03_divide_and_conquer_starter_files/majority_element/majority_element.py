# Uses python3
import sys

def find_occurance(a,x):
    count = 0
    for i in a:
        if i==x:
            count = count + 1
    return(count)

def get_majority_element(a, left, right):
    # Empty set
    if left == right: 
        return -1
    
    # There is only element in the set
    if left + 1 == right:
        return a[left]
        
    #write your code here
    middle = int((left + right) / 2)
    
    x1 = get_majority_element(a, left, middle)
    x2 = get_majority_element(a, middle, right)
    
    # Note: a[i] is assumed to be greater than or equal to 0.
    if x1 >= 0:
        x1_cnt = find_occurance(a,x1)
        if x1_cnt > int(len(a)/2):
            return x1
        else:
            return -1
    elif x2 >= 0:
        x2_cnt = find_occurance(a,x2)
        if x2_cnt > int(len(a)/2):
            return x2
        else:
            return -1
    else:
        return -1
             
    #return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
