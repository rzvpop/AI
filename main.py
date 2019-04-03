from Controller import Controller
from Problem import Problem
from State import State
from UI import UI


def main():
    init_state = State
    problem = Problem(init_state)
    ctrl = Controller(problem)
    view = UI(ctrl)

    view.menu()


main()
