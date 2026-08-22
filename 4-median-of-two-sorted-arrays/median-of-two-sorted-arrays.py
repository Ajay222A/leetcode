class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        arr.extend(nums1)
        arr.extend(nums2)
        arr.sort()
        print(arr)
        le=len(arr)
        mid=math.ceil((le)/2)
        if le%2!=0:
            return arr[mid-1]
        else:
            r=(arr[mid-1]+arr[mid])/2
            return r