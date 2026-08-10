class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # restrain smallest to the beginning
        # key idea: medians MUST have equal elements on L and R
        
            # how many elements are in our left partition? from A
            # take half - x from B for the rest
        # validate the partition, all left should be less than all right on the ends of the partitions

        # key idea: there is guranteed ONE median in the question
        # in perfect partitions, the max on the left and min on the right
            # are the median since both partitions are sorted

        # bin search applies to HOW MANY elements we take
           # occurs on our min array to reduce time complexity
           # restrains possible solutions on taking 0 to len(a) elems  

        a, b = nums1, nums2
        half = (len(a) + len(b)) // 2

        # ensure our smallest array is always a
        if len(a) > len(b):
            a, b = b, a

        l, r = 0, len(a) - 1

        while True:
            m = (l + r) // 2

            # m + 1 how many elems from A we take
            x = half - m - 2
            
            # if m goes below 0, all e in A > all p in B == no e from A in left partition
            # therefore la is guranteed smaller than rb so set to -inf
            la = a[m] if m >= 0 else float("-inf")
            lb = b[x] if x >= 0 else float("-inf")

            # if m or x goes above the indices of their array
            # continously adding parts of the array to the left partition
            # gurantees e in A < all p in B
            ra = a[m + 1] if (m + 1) < len(a) else float("inf")
            rb = b[x + 1] if (x + 1) < len(b) else float("inf")

            if la > rb:
                r = m - 1
            elif lb > ra:
                l = m + 1
            else:
                # odd
                if (len(a) + len(b)) % 2:
                    return min(ra, rb)
                else:
                    return (max(la, lb) + min(ra, rb)) / 2

        