class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i_1 = 0
        i_2 = 0

        while i_1 < m and i_2 < n:
            if nums1[i_1] > nums2[i_2]:
                nums1.insert(i_1, nums2[i_2])
                nums1.pop()
                m += 1
                i_2 += 1
            i_1 += 1

        if i_2 < n:
            for i in range(n - i_2):
                nums1[m + i] = nums2[i_2 + i]
