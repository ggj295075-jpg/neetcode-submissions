class Solution:
    def isValid(self, s: str) -> bool:
        val = []
        sav = {"]": "[", ")": "(", "}": "{"}

        for i in s:
            if i in sav:
                if val and val[-1] == sav[i]:
                    val.pop()
                else:
                    return False
            else:
                val.append(i)
        return True if not val else False
