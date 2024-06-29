class Solution(object):
    def findMedianSortedArrays(self, nums_1, nums_2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """        
        def cycle(tar_ind, nums1, nums2, even=False, flag=1):
            if tar_ind <= 0: 
                num1 = min((x[0] for x in (nums1,nums2) if x))
                if tar_ind <  0:
                    return num1
                else:
                    if flag: 
                        num2 = cycle(1, nums1, nums2, flag=0)
                    else: 
                        return num1
                    if not even: 
                        return num2
                    else: 
                        return (float(num1)+float(num2))/2
            else:
                tar_ind1 = int((tar_ind+1)/2-1)
                if len(nums2)>tar_ind1:
                    if (len(nums1)<=tar_ind1 or nums1[tar_ind1] > nums2[tar_ind1]) : 
                        nums1, nums2 = nums2, nums1
                nums1 = nums1[tar_ind1+1:]
                tar_ind = tar_ind - tar_ind1 -1
                return cycle(tar_ind, nums1, nums2, even, flag)

        n1 = len( nums_1)
        n2 = len( nums_2)
        tar_ind0 = int((n1+n2)/2-1) # &int((n1+n2)/2) if even   
        if (n1+n2) %2 ==0:
            return cycle(tar_ind0, nums_1, nums_2,even=True)
        else: 
            return cycle(tar_ind0, nums_1, nums_2)
            return cycle(tar_ind0, nums_1, nums_2)