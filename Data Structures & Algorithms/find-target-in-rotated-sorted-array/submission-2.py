class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(nums, target):
            l, r = 0, len(nums) - 1

            while l <= r:
                m = (r + l) // 2

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1

        l, r = 0, len(nums) - 1
        res = nums[l]
        cut = 0
        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < res:
                    res = nums[l]
                    cut = l                
                break
            m = (r + l) // 2
            if nums[m] < res:
                res = nums[m]
                cut = m

            # 2 sorted parts of array
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        # print(res,cut)

        part1 = nums[0:cut]
        part2 = nums[cut:]

        # print(part1)
        # print(part2)

        search1 = binSearch(part1, target)
        search2 = binSearch(part2, target)

        search2 += len(part1) if search2 > -1 else 0

        return max(search1, search2)

                
            

  