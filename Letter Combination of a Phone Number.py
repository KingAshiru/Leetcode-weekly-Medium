class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_num = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        res = []
        if len(digits) == 0:
            return []
        
        def backtrack(index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            cur_num = phone_num[digits[index]]
            for char in cur_num:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()
            
        backtrack(0, [])
        return res
