class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_index = word.find(ch)
        if (ch_index == -1):
            return word

        result = []
       
        for i in range(0, len(word)):
            if (i <= ch_index):
                result.append(word[ch_index - i])
            else:
                result.append(word[i])

        return ''.join(result)
            
            