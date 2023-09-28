'''
Time Complexity: O(n log(k))  where is the size of array
Space Complexity: O(k)  where k is largest element
'''
import heapq as pq


def kth_largest(arr_lst, k):
    min_heap = []
    pq.heapify(min_heap)
    size = len(arr_lst)
    for i in range(k):
        pq.heappush(min_heap, arr_lst[i])           # add first k elem in priority queue
    
    for i in range(k, size):
        if arr_lst[i] > min_heap[0]:
            pq.heappop(min_heap)
            pq.heappush(min_heap, arr_lst[i])
    return min_heap[0]


def main():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    k = int(input())
    ans = kth_largest(lst, k)
    print(ans)


if __name__ == '__main__':
    main()