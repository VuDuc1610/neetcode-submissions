class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def helper(lst, remain, idx):
            if remain == 0:
                ans.append(lst[:])
                return
            if remain < 0 or idx >= len(candidates):
                return
            
            num = candidates[idx]
            lst.append(num)
            helper(lst, remain - num, idx+1)
            lst.pop()

            while idx + 1 < len(candidates) and num == candidates[idx+1]:
                idx += 1
            helper(lst, remain, idx+1)
        
        helper([], target, 0)
        return ans