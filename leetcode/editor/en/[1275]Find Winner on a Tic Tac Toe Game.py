# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. 
# 
#  Here are the rules of Tic-Tac-Toe: 
# 
#  
#  Players take turns placing characters into empty squares (" "). 
#  The first player A always places "X" characters, while the second player B al
# ways places "O" characters. 
#  "X" and "O" characters are always placed into empty squares, never on filled 
# ones. 
#  The game ends when there are 3 of the same (non-empty) character filling any 
# row, column, or diagonal. 
#  The game also ends if all squares are non-empty. 
#  No more moves can be played if the game is over. 
#  
# 
#  Given an array moves where each element is another array of size 2 correspond
# ing to the row and column of the grid where they mark their respective character
#  in the order in which A and B play. 
# 
#  Return the winner of the game if it exists (A or B), in case the game ends in
#  a draw return "Draw", if there are still movements to play return "Pending". 
# 
#  You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the
#  grid is initially empty and A will play first. 
# 
#  
#  Example 1: 
# 
#  
# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: "A" wins, he always plays first.
# "X  "    "X  "    "X  "    "X  "    "X  "
# "   " -> "   " -> " X " -> " X " -> " X "
# "   "    "O  "    "O  "    "OO "    "OOX"
#  
# 
#  Example 2: 
# 
#  
# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: "B" wins.
# "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
# "   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
# "   "    "   "    "   "    "   "    "   "    "O  "
#  
# 
#  Example 3: 
# 
#  
# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.
# "XXO"
# "OOX"
# "XOX"
#  
# 
#  Example 4: 
# 
#  
# Input: moves = [[0,0],[1,1]]
# Output: "Pending"
# Explanation: The game has not finished yet.
# "X  "
# " O "
# "   "
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= moves.length <= 9 
#  moves[i].length == 2 
#  0 <= moves[i][j] <= 2 
#  There are no repeated elements on moves. 
#  moves follow the rules of tic tac toe. 
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        row = [0] * 3
        col = [0] * 3
        diag1 = 0
        diag2 = 0

        for k, move in enumerate(moves):
            i, j = move
            if k % 2 == 0:
                row[i] += 1
                col[j] += 1
                if i == j: diag1 += 1
                if i + j == 2: diag2 += 1
                if row[i] == 3 or col[j] == 3 or diag1 == 3 or diag2 == 3: return 'A'
            else:
                row[i] -= 1
                col[j] -= 1
                if i == j: diag1 -= 1
                if i + j == 2: diag2 -= 1
                if row[i] == -3 or col[j] == -3 or diag1 == -3 or diag2 == -3: return 'B'
        return 'Draw' if len(moves) == 9 else 'Pending'
        
# leetcode submit region end(Prohibit modification and deletion)
