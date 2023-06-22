class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ''


        if len(word1) >= len(word2):
            for index, char in enumerate(word1):
                mergedString += char
                if index < len(word2):
                    mergedString += word2[index]
        else:
            for index, char in enumerate(word2):
                if index < len(word1):
                    mergedString += word1[index]
                mergedString += char


        return mergedString

            

