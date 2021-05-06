class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        nums3 = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                nums3.append(nums1[p1])
                p1 += 1
            else:
                nums3.append(nums2[p2])
                p2 += 1
        while p1 < len(nums1):
            nums3.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            nums3.append(nums2[p2])
            p2 += 1
        if len(nums3) % 2 == 0:
            print(nums3)
            return (nums3[(len(nums3) // 2) - 1] + nums3[len(nums3) // 2]) / 2
        else:
            return nums3[len(nums3) // 2]