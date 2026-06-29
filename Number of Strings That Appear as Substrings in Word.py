#Number of Strings That Appear as Substrings in Word
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
      c = 0
      for p in patterns:
        if word in patterns:
          c += 1
       return 0
