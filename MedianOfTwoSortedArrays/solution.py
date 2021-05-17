class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = []
        if len(nums1) < len(nums2):
            small_arr = nums1
            big_arr = nums2
        else:
            small_arr = nums2
            big_arr = nums1
            
        i = 0
        j = 0
        while j < len(small_arr) and i < len(big_arr):
            bg_num = big_arr[i]
            sm_num = small_arr[j]
            if sm_num < bg_num:
                merged_arr.append(sm_num)
                j += 1
            elif sm_num == bg_num:
                merged_arr.append(sm_num)
                merged_arr.append(bg_num)
                i += 1
                j += 1
            else:
                merged_arr.append(bg_num)
                i += 1

        if j < len(small_arr):
            merged_arr.extend(small_arr[j:])
        elif i < len(big_arr):
            merged_arr.extend(big_arr[i:])
                            
        l = len(merged_arr)
        
        if l % 2 == 1:
            index = int((l-1)/2)
            return float(merged_arr[index])
        
        half = int(l/2)
        i, j = half-1, half
        return (merged_arr[i] + merged_arr[j])/2
  
        
        
        