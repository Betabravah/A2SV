class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[m+i] = nums2[i]

        # nums1.sort()

        position = n + m - 1
        left, right = m-1, n-1

        while position >= 0:
            if left >= 0 and right >= 0:
                if nums1[left] > nums2[right]:
                    nums1[position], nums1[left] = nums1[left], nums1[position]
                    left -= 1
                    position -= 1

                else:
                    nums1[position], nums2[right] = nums2[right], nums1[position]
                    right -= 1
                    position -= 1
            else:
                if left >= 0:
                    nums1[position], nums1[left] = nums1[left], nums1[position]
                    left -= 1
                    position -= 1
                elif right >= 0:
                    nums1[position], nums2[right] = nums2[right], nums1[position]
                    right -= 1
                    position -= 1

