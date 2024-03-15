class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * (len(nums) + 1)
        suffix_arr = [1] * (len(nums) + 1)
    

        for i in range(1, len(nums)+1):
            prefix_arr[i] = prefix_arr[i - 1] * nums[i - 1]
            suffix_arr[len(prefix_arr) - i -1] = suffix_arr[len(prefix_arr) - i] * nums[len(prefix_arr) - i -1]


        answer = []
        for i in range(1, len(nums)+1):
            answer.append(prefix_arr[i - 1] * suffix_arr[i])
        return answer


        
        
