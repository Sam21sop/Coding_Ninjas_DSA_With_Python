import heapq as pq


def k_smallest(arr_lst, k):
    max_heap = []
    pq.heapify(max_heap)
    size = len(arr_lst)
    
    for i in range(k):
        pq.heappush(max_heap, -1 * arr_lst[i])            # Add first k elem to max heap by negating elem

    for index in range(k, size):
        if -1 * arr_lst[index] > max_heap[0]:
            pq.heappop(max_heap)
            pq.heappush(max_heap, -1 * arr_lst[index])

    positive_ele = [i * -1 for i in max_heap]
    return positive_ele


def main():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    k = int(input().strip())
    ans = k_smallest(lst, k)
    ans.sort()
    print(*ans, sep=' ')


if __name__ == '__main__':
    main()