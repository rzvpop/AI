from Problem import Problem


class Controller:
    def __init__(self, problem):
        self._problem = problem
        self._problem.readFromFile("file.txt")
        self._m = self._problem.getInitState().getMatrix()
        print(self._m)

    def getProblem(self):
        return self._problem

    def gBack(self, free, cnt):
        min_len_pos_index = self._problem.heuristic(self._m, free)

        for i in self._problem.check(self._m, free[min_len_pos_index][0]):
            free[min_len_pos_index][1] = i
            self._m[free[min_len_pos_index][0][0]][free[min_len_pos_index][0][1]] = i

            for k in self._m:
                print(k)
            print()

            if cnt == (len(free) - 1):
                return self._m
            else:
                res = self.gBack(free, cnt + 1)
                if res is not None:
                    return self._m
                free[min_len_pos_index][1] = 0
                self._m[free[min_len_pos_index][0][0]][free[min_len_pos_index][0][1]] = 0

    def back(self, free, cnt):
        for i in self._problem.check(self._m, free[cnt][0]):
            free[cnt][1] = i
            self._m[free[cnt][0][0]][free[cnt][0][1]] = i

            for k in self._m:
                print(k)
            print()

            if cnt == (len(free) - 1):
                return self._m
            else:
                res = self.back(free, cnt + 1)
                if res is not None:
                    return self._m
                free[cnt][1] = 0
                self._m[free[cnt][0][0]][free[cnt][0][1]] = 0

