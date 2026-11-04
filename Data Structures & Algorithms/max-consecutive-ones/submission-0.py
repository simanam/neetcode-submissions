class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #go through loop
        #see first value at i index, if its 1
        #then compare it to next value i+1
        #if it is same create variable which start at 1 and 1 to one
        #then to next one if its different then start new variable and 1 to it 
        #every time its 0 skip 
        #once react at the end of the array , compare all the values 
        totalConsecutiveOnes = []
        counter = 0

        for i in nums:
            if i == 1:
                counter += 1 
            else:
                totalConsecutiveOnes.append(counter)
                counter = 0 
        totalConsecutiveOnes.append(counter)

        return max(totalConsecutiveOnes)



                
