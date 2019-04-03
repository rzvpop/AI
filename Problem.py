import math
from State import State


class Problem:
    def __init__(self, initState):
        self._initState = initState
        self._finState = []

    def getInitState(self):
        return self._initState

    def getFinState(self):
        return self._finState

    def readFromFile(self, file_name):
        m = []

        with open(file_name, 'r') as fp:
            line = fp.readline()

            while line:
                l_str = line.split(' ')
                l_nr = [(lambda x: int(x))(x) for x in l_str]
                m += [l_nr]

                line = fp.readline()

        self._initState = State(m)

    def check(self, m, pos):
        N = len(m)
        n = math.sqrt(N)
        choices = []
        cut = []

        for i in range(N):
            if m[pos[0]][i] != 0:
                cut += [m[pos[0]][i]]
            if m[i][pos[1]] != 0:
                cut += [m[i][pos[1]]]

        x = int(pos[0] / n) * int(n)
        y = int(pos[1] / n) * int(n)
        for i in range(int(n)):
            for j in range(int(n)):
                if m[x + i][y + j] != 0:
                    cut += [m[x + i][y + j]]

        for i in range(1, N + 1):
            if i not in cut:
                choices += [i]

        return choices


    def heuristic(self, m, free):
        min_len_pos_index = 0
        min_choices = 10

        for i in range(len(free)):
            if free[i][1] == 0:
                if min_choices > len(self.check(m, free[i][0])):
                    min_len_pos_index = i
                    min_choices = len(self.check(m, free[i][0]))

        return min_len_pos_index