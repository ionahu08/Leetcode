class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx1, idx2 = 0, 0
        temp = 0
        while True:
            if idx1 >= len(word) or idx2 >= len(abbr):
                break
            if not abbr[idx2].isdigit():
                idx1 += temp
                if idx1 >= len(word):
                    return False
                temp = 0
                if word[idx1] != abbr[idx2]:
                    return False
                else:
                    idx1 += 1
                    idx2 += 1
            else:
                if temp == 0 and abbr[idx2]=="0":
                    return False

                temp = temp*10 + int(abbr[idx2])
                idx2 += 1

        idx1 += temp
        if idx1 == len(word) and idx2 == len(abbr):
            return True
        return False






        