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

def partition3(a, l, r):
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

def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m_left,m_right = partition3(a, l, r)
    randomized_quick_sort3(a, l, m_left - 1);
    randomized_quick_sort3(a, m_right + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #randomized_quick_sort(a, 0, n - 1)
    randomized_quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
