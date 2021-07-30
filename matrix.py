
import numpy as np

class matrix:
    mat = []
    det = 0

    def matrix(self):
        return

    def matrix(self, n, m):
        for i in range(0, n):
            for j in range(0, m):
                self.mat[i][j] = 0

    def set_matrix(self, x):
        self.mat = x

    def get_matrix(self):
        return self.mat

    def product(self, m2):
        return

    def transpose(self):
        tp  = []
        for i in range(0, len(self.mat)):
            x = []
            for j in range(0, len(self.mat[i])):
                x.append(0)
            tp.append(x)

        for r in range(0, len(self.mat)):
            for c in range(0, len(self.mat[r])):
                tp[r][c] = self.mat[c][r]

        return tp


    def find_own_det(self):
        self.find_det(self.mat)

    def find_det(self, m):
        if len(m) != len(m[0]):
            return None

        if len(m) == 2:
            return (m[0][0]*m[1][1]) - (m[0][1]*m[1][0])

        for i in range(0, len(m)):
            d = np.delete(m, 0, 0)
            d = np.delete(d, i, 1)
            if i % 2 == 0:
                self.det = self.det - (m[0][i]*self.find_det(d))
            else:
                self.det = self.det + (m[0][i]*self.find_det(d))

        return self.det

    def to_string(self):
        strmat = ""

        for i in self.mat:
            for j in i:
                strmat += (j + " ")
            strmat += "\n"

        return strmat
