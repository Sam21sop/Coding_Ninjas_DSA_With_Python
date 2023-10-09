import heapq as pq

def peek_value(heap):
    peak_v = pq.heappop(heap)
    pq.heappush(heap, peak_v)
    return peak_v


def isEmpty(heap):
    if len(heap) != 0:
        return False
    return True


def k_largest(arr_lst:[int], k:int):
    min_heap = []                               # create empty min_heap
    for i in range(k):                          # push k element in heap
        pq.heappush(min_heap, arr_lst[i])

    for i in range(k, len(arr_lst)):            # iterate over the rmaining arr
        if arr_lst[i] > peek_value(min_heap):   # Check current elem is greter than peak elem
            pq.heappop(min_heap)                # remove min element from min heap
            pq.heappush(min_heap, arr_lst[i])   # push current elem
    
    ans = []
    while not isEmpty(min_heap):                # create empty list to store k largest elem
        ans.append(pq.heappop(min_heap))        
    return ans


def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input().strip())
    res = k_largest(arr, k)
    for i in res:
        print(i)


if __name__ == '__main__':
    main()