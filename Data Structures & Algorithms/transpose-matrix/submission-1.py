class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = []
        length = len(matrix)

        for i in range(len(matrix[0])):
            list_for_append = [matrix[z][i] for z in range(length)]
            new_matrix.append(list_for_append)
        return new_matrix    

