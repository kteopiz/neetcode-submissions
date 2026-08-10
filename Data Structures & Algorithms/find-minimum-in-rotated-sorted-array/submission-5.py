class Solution:
    def findMin(self, nums: List[int]) -> int:
        # KEY INFO:
        # assuming a wrap occurred, the pivot is where the break in ordering occurs
        # additionally wherever the pivot is we also know is where the MIN exists
        # the pivot cannot exist in a part of the array where ordering HOLDS 
        
        # also assuming a wrap occured, the biggest numbers will be rotated to the left side of the array
        # two distinct parts will exist, each respectively sorted, seperated by a pivot

        # set arbitrarily, must exist in the array somewhere
        res = nums[0]

        l,r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            mid = (r + l) // 2
            res = min(res, nums[mid])
            # if the mid proves greater than what is before it, ordering must hold in this portion
            if nums[mid] >= nums[l]:
                l = mid + 1
            # ordering does not hold in this part of the array, the pivot must exist here
            else:
                r = mid - 1
        return res