class Solution(object):
    
    # List of characters with index of their values
    list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    
    # Do the calculation
    def isSumEqual(self, firstWord, secondWord, targetWord):

        if self.calcChars(firstWord) + self.calcChars(secondWord) == self.calcChars(targetWord):
            return True
        else:
            return False
        
    # Return the number given by the index of each character
    def calcChars(self, word):
        val = ""
        for char in word:
            # Must be added like a string not like int - E.g. NOT 2+1 but 21
            val += str(self.list.index(char))
        # Return as int so calculation can be performed
        return int(val)