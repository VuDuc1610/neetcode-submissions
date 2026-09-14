class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total//2
        if len(A) > len(B):
            A, B = B, A
        i, j = -1, len(A)-1
        while True:
            midA = i + (j-i)//2
            midB = half-midA-2
            A_left = A[midA] if midA >= 0 else float('-inf')
            A_right = A[midA+1] if midA+1 < len(A) else float('inf')
            B_left = B[midB] if midB >= 0 else float('-inf')
            B_right = B[midB+1] if midB + 1 < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 0:
                    ans = (max(A_left,B_left)+min(A_right,B_right))/2
                    return ans
                else:
                    return min(A_right, B_right)
            elif A_left > B_right:
                j = midA-1
            else:
                i = midA + 1