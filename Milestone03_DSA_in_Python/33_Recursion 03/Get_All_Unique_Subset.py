class Solution:
    def subset_with_duplicate(self, nums:list[int]):
        def _helper(start_index, subset):
            result.append(subset[:])
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                _helper(i+1, subset)
                subset.pop()
        result = []
        nums.sort()
        _helper(0, [])
        return result
    

def main():
    n = int(input())
    nums = list(map(int, input().strip().split()))
    obj = Solution()
    ans = obj.subset_with_duplicate(nums)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
