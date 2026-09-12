class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array = list()
        res = 0
        for i in operations:
            if i == "+":
                array.append(array[-1] + array[-2])
            elif i == "C":
                array.pop()
            elif i == "D":
                array.append(array[-1] * 2)
            else: array.append(int(i))
        for z in array:
            res += z
        return res