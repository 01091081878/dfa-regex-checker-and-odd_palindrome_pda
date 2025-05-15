class PDA:
    def __init__(self):
        self.stack = []
        
    def is_palindrome_odd(self, s: str) -> bool:
        if len(s) % 2 == 0:
            return False  
        mid = len(s) // 2

        
        for i in range(mid):
            self.stack.append(s[i])
        
        
        i = mid + 1
        
       
        
        while i < len(s):
            if not self.stack or s[i] != self.stack.pop():
                return False
            i += 1
        
        return len(self.stack) == 0
