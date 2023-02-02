#!/usr/bin/python3
  self.x = [0 for i in range(n + 1)]
ion = []
ed all 4 Queens (A solution was found)

 - 1    else:
 + 1)
        return self.res


# N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a be at least 4")
    sys.exit(1)

queen = NQueen(N)
res = queen.nQueen(1)
INSIDE LOOP) ""N Queen Problem """

    def __init__(self, n):
        """ Global Variables "ced in i column (True)
        or if the are attacking queens in row or diagonal (False)
        """

        # j checks from 1 to k - 1 (Up to p same diagonal
            if self.x[j] == i or \      return 0
        return 1

    def nQueen(self, k):
        """ Tries to place every queen in the board
        Args:
        k: starting     # i goes from column 1 to column n (1st column is 1st index)
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # Queen can be placed in i column
                self.x[k] = i
                if k == self.n:
