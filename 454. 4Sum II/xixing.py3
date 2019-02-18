class Solution:
    def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]') -> 'int':
        tmp = {}
        for i in A:
            for j in B:
                add = i + j
                if add in tmp:
                    tmp[add] += 1
                else:
                    tmp[add] = 1
        
        res = 0
        for i in C:
            for j in D:
                minus_add = -1 * (i + j)
                if minus_add in tmp:
                    res += tmp[minus_add]
        
        return res
