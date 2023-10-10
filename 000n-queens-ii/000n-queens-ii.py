class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.cols = set()
        self.ds = set()
        self.antids = set()
        return self.backtrack_nqueen(0, 0)
        
    
    def backtrack_nqueen(self, row, count):
        for col in range(self.n):
            # iterate through columns at the curent row.
            if self.is_not_under_attack(row, col):
                # explore this partial candidate solution, and mark the attacking zone
                self.place_queen(row, col)
                if row + 1 == self.n:
                    # we reach the bottom, i.e. we find a solution!
                    count += 1
                else:
                    # we move on to the next row
                    count = self.backtrack_nqueen(row + 1, count)
                # backtrack, i.e. remove the queen and remove the attacking zone.
                self.remove_queen(row, col)
        return count
    
    def is_not_under_attack(self, row, col):
        if col not in self.cols and row+col not in self.ds and row-col not in self.antids:
            return True
        return False
        
    def place_queen(self, r, c):
        # col
        self.cols.add(c)
        
        # hill diagonal 
        self.ds.add(r+c)
        
        # dale diagonal
        self.antids.add(r-c)
        
    def remove_queen(self, r, c):
        # col
        self.cols.remove(c)
        
        # hill diagonal 
        self.ds.remove(r+c)
        
        # dale diagonal
        self.antids.remove(r-c)
        