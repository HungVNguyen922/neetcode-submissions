class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the match action is  on the current num and its complement
        # instead of using a dict to store indices we can grab those values from 
        visited = {}

        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in visited:
                return [visited[goal], i]
            else:
                visited[nums[i]] = i
        