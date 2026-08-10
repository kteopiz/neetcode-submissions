class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1

        # Edges: no rotation, array size 1
        if nums[l] < nums[r] or l == r:
            return nums[l]

        # Assume from now there has been a rotation between 1 and n-1

        # max more than neigbors
        # min less than neighbors
        # mid num is less than one, more than one
        while l <= r:
            mid = (r + l) // 2
            curr = nums[mid]
            front = mid + 1
            back = mid - 1
            
            print(mid, nums[front], nums[back])

            if curr < nums[front] and curr < nums[back]:
                return curr
            elif curr > nums[front] and curr > nums[back]:
                return nums[(mid + 1) % len(nums)]
            else:
                print(abs(curr - nums[r]), abs(curr - nums[l]))
                if abs(curr - nums[r]) > abs(curr - nums[l]):
                    l = front
                else:
                    r = back
        
        # ?
        return nums[l]
        




