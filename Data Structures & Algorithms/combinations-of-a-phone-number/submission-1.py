class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res=[""]

        char ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        for digit in digits:
            tmp=[]
            for curstr in res:
                for c in char[digit]:
                    tmp.append(curstr+c)
            res=tmp
        return res