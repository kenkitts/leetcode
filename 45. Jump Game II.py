class Solution:
    def jump(self, nums) -> int:
        if len(nums) == 1:
            return 0

        jump_count = 0
        index = 0
        end = len(nums) - 1

        while index < end:
            jump_distance = nums[index]
            max_jump = 0
            if jump_distance >= end - index:
                jump_count += 1
                return jump_count

            for i in range(index + 1, index + 1 + jump_distance):
                jump_tally = i + nums[i]
                if jump_tally > max_jump:
                    max_jump = jump_tally
                    index = i
            jump_count += 1
        return jump_count

l = [2,2,4,1,50,3,1,66,43,21]
s = Solution()
print(s.jump(l))