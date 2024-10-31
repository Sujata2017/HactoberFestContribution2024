https://leetcode.com/problems/unique-paths-ii/description/

63. Unique Paths II
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle. Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])

        if(obstacleGrid[0][0]==1 or obstacleGrid[n-1][m-1]==1):
            return 0    
        obstacleGrid[0][0] = 1

        for i in range(1, n):
            if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0

        for j in range(1,m):
            if obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1:
                obstacleGrid[0][j] = 1
            else:
                obstacleGrid[0][j] = 0


        for i in range(1,n):
            for j in range(1,m):
                if(obstacleGrid[i][j]==0):
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=0
                  
        return obstacleGrid[-1][-1]            
         
