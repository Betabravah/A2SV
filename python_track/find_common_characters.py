class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        offset = ord('a')
        letterCount = [0] * 26
        for letter in words[0]:
            ascii = ord(letter)
            letterCount[ascii - offset] += 1

        
        for word in words:
            newCount = [0] * 26
            for letter in word:
                ascii = ord(letter)
                newCount[ascii - offset] += 1
            for idx in range(26):
                letterCount[idx] = min(letterCount[idx], newCount[idx])
        
        chars = []
        for idx, count in enumerate(letterCount):
            if count != 0:
                char = chr(idx + offset)
                for i in range(count):
                    chars.append(char)

        return chars

