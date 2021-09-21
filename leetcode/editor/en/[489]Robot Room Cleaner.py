# Given a robot cleaner in a room modeled as a grid. 
# 
#  Each cell in the grid can be empty or blocked. 
# 
#  The robot cleaner with 4 given APIs can move forward, turn left or turn right
# . Each turn it made is 90 degrees. 
# 
#  When it tries to move into a blocked cell, its bumper sensor detects the obst
# acle and it stays on the current cell. 
# 
#  Design an algorithm to clean the entire room using only the 4 given APIs show
# n below. 
# 
#  
# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cel
# l.
#   boolean move();
# 
#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();
# 
#   // Clean the current cell.
#   void clean();
# }
#  
# 
#  Example: 
# 
#  
# Input:
# room = [
#   [1,1,1,1,1,0,1,1],
#   [1,1,1,1,1,0,1,1],
#   [1,0,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0,0],
#   [1,1,1,1,1,1,1,1]
# ],
# row = 1,
# col = 3
# 
# Explanation:
# All grids in the room are marked by either 0 or 1.
# 0 means the cell is blocked, while 1 means the cell is accessible.
# The robot initially starts at the position of row=1, col=3.
# From the top left corner, its position is one row below and three columns righ
# t.
#  
# 
#  Notes: 
# 
#  
#  The input is only given to initialize the room and the robot's position inter
# nally. You must solve this problem "blindfolded". In other words, you must contr
# ol the robot using only the mentioned 4 APIs, without knowing the room layout an
# d the initial robot's position. 
#  The robot's initial position will always be in an accessible cell. 
#  The initial direction of the robot will be facing up. 
#  All accessible cells are connected, which means the all cells marked as 1 wil
# l be accessible by the robot. 
#  Assume all four edges of the grid are all surrounded by wall. 
#  
#  Related Topics Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]


        def dfs(robot, x, y, d, visited):
            #print(x, y, d)
            robot.clean()
            visited.add((x, y))
            for i in range(4):
                nd = (d + i) % 4
                nx = x + dirs[nd][0]
                ny = y + dirs[nd][1]
                if (nx, ny) not in visited and robot.move():
                    dfs(robot, nx, ny, nd, visited)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()

        dfs(robot, 0, 0, 0, visited)
        
# leetcode submit region end(Prohibit modification and deletion)
