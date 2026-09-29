class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for b in bills:
            if b == 5:
                fives += 1
                continue

            if b == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1

                continue

            if (tens >= 1 and fives >= 1):
                tens -= 1
                fives -= 1
                continue
            
            if (fives >= 3):
                fives -= 3
                continue
            
            return False

        return True

    
            
            
            

