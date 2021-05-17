from types import List

class Solution:
    def __init__(self):
        self.num_to_letters = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        
        letters = [l for l in self.num_to_letters[digits[0]]]
        for d in digits[1:]:
            letters = [w + l for w in letters for l in self.num_to_letters[d]]
            
        return letters