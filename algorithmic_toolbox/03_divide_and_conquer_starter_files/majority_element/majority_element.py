# Uses python3
import sys

def find_occurence(a,x):
    count = 0
    for i in a:
        if i==x:
            count = count + 1
    return(count)

# Note: 
#    The requirement to the return is:
#    0--no majority number;
#    1--there is majority number;
# No need to return who is the majority number or the exact occurance of the 
# majority number, if there is one.
    
def get_majority_element(a, left, right):
    # Empty set
    if left == right: 
        return -1
    
    # There is only element in the set
    # Note: the input is a[left:right), i.e, the right boundary is not inclusive.
    if left + 1 == right:
        return a[left]
        
    #write your code here
    middle = int((left + right) / 2)
    
    x1 = get_majority_element(a, left, middle)
    x2 = get_majority_element(a, middle, right)
    
    # Note: a[i] is assumed to be greater than or equal to 0.
    if x1 >= 0:        
        x1_cnt = a[left:right].count(x1)
        #print('S1: ', x1, x1_cnt, middle)
        if x1_cnt > (right - left)/2:
            return x1  # x1 is majority
    if x2 >= 0:
        x2_cnt = a[left:right].count(x2)
        #print('S2: ', x2, x2_cnt, middle)
        if x2_cnt > (right - left)/2:
            return x2  # x2 is majority    

    #case-1# No majority element in either sub-problem.             
    #case-2# Although there is majority sub-problem in either one or both 
    #        sub-problem, but no global majority element.
    return -1 

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #print(a)
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
