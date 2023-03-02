class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        
        print(prefix)
        mono_queue = deque()
        minLen = len(nums) + 1
        for right in range(len(nums) + 1):
            if not mono_queue:
                mono_queue.append(right)

            else:

                while mono_queue and prefix[right] < prefix[mono_queue[-1]]:
                    mono_queue.pop()
                mono_queue.append(right)


                while mono_queue and prefix[mono_queue[-1]] - prefix[mono_queue[0]] >= k:
                    length = mono_queue[-1] - mono_queue[0]
                    minLen = min(minLen, length)
                    mono_queue.popleft()

                

        if minLen == len(nums) + 1:
            return -1
        return minLen
