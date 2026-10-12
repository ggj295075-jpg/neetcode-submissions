class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []

        def binSearch(array, target):
            l, r = 0, len(array) - 1
            while l <= r:
                m = l + ((r-l)//2)

                if array[m] < target:
                    l = m+1
                elif array[m] > target:
                    r = m-1
                else:
                    return res.append(True)
            return res.append(False)
        for i in range(len(matrix)):
            binSearch(matrix[i], target)
        for i in res:
            if i == True:
                return True
        return False