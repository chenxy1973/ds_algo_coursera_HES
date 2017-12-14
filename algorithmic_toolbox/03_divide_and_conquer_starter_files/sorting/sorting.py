# Uses python3
import sys
import random

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]  # WHY??? chenxy@2017-12-14
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

# Failed at 15/23 time exceeded limit, 17.52/11.00
def partition3_0(a, l, r):
    #write your code here
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]  # WHY??? chenxy@2017-12-14
    
    m_right = j
    
    #Further, search for m_left
    for i in range(l,m_right):
        if a[m_right-1-i] == x:
            j = j - 1
            a[m_right-1-i], a[j] = a[j], a[m_right-1-i]
            
    m_left = j
        
    return m_left, m_right

#Failed case #4/23: time limit exceeded (Time used: 21.98/11.00, memory used: 29163520/536870912.)
def partition3_1(a, l, r):
    #write your code here
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]  # WHY??? chenxy@2017-12-14
    
    m_right = j
    #print("A: ",m_right,a)
    #Further, search for m_left
    swap  = False
    left  = 0
    right = m_right - 1
    #while left <= right:--> Failed for the case of [10 9 8 7 6 5 4 3 2 1].
    while left <= right:
        if a[left] == x:
            #print("B: ",left, right)
            swap = False
            while right > left:
                if a[right] < x:
                    a[left], a[right] = a[right], a[left]
                    right = right - 1
                    left  = left  + 1
                    swap  = True
                    break
                right = right - 1 
            if swap == False:
                break    
        else:
            left = left + 1
            
    m_left = left
    #print("C: ",m_left, m_right, a)    
    return m_left, m_right

def partition3_2(a, l, r):
    #write your code here
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]  # WHY??? chenxy@2017-12-14
    
    m_right = j
    #print("A: ",m_right,a)
    #Further, search for m_left
    swap  = False
    left  = 0
    right = m_right - 1
    #while left <= right:--> Failed for the case of [10 9 8 7 6 5 4 3 2 1] as above-mentioned.
    while left <= right:
        if a[left] == x:
            #print("B: ",left, right)
            swap = False
            while right > left:
                if a[right] < x:
                    a[left], a[right] = a[right], a[left]
                    right = right - 1
                    left  = left  + 1
                    swap  = True
                    break
                right = right - 1 
            if swap == False:
                break    
        else:
            left = left + 1
            
    m_left = left
    #print("C: ",m_left, m_right, a)    
    return m_left, m_right

def randomized_quick_sort3(a, l, r):
    #print("000--> ",a, l, r)
    if l >= r or l < 0:
        return
    #k = random.randint(l, r)
    #a[l], a[k] = a[k], a[l]
    #use partition3
    m_left,m_right = partition3_2(a, l, r)
    randomized_quick_sort3(a, l, m_left - 1);
    randomized_quick_sort3(a, m_right + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #randomized_quick_sort(a, 0, n - 1)
    randomized_quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
