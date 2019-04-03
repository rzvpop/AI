class UI:
    def __init__(self, ctrl):
        self._ctrl = ctrl

    def menu(self):
        m = self._ctrl.getProblem().getInitState().getMatrix()

        free_pos = []
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 0:
                    free_pos += [[(i, j), m[i][j]]]

        stop = 0
        while stop == 0:
            print("Choose:")
            print("1. BFS")
            print("2. GBFS")
            opt = input(">>")
            opt = int(opt)

            if opt == 1:
                self._ctrl.back(free_pos, 0)
            elif opt == 2:
                self._ctrl.gBack(free_pos, 0)

            stop = input("Continue?(y/n)")
            if stop == "n":
                stop = 0
