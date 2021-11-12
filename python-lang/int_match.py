class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        match = []
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i == j:
                    continue  #used break before, wrong flow control
                elif nums[i] + nums[j] == target:
                    print(i, j)
                    match.append(i)
                    match.append(j)
        return match

if __name__ == "__main__":
    answer = Solution().twoSum([3, 2, 4, 5, 9, 15], 6)
    print(answer)