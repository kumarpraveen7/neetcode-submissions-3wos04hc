class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        x = 0
        y = n-1

        while(x<m and y>=0):
            if(matrix[x][y] < target):
                x+=1
            elif(matrix[x][y] > target):
                y-=1
            else:
                return True
        return False
        