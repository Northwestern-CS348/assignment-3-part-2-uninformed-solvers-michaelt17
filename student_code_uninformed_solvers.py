
from solver import *

class SolverDFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Depth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """

        # print(self.gm.getMovables())
        # print(self.victoryCondition)
        hasNewNode = False

        if self.currentState.state == self.victoryCondition:
            return True

        # print(self.currentState.state)

        currDepth = self.currentState.depth
        oldState = self.currentState

        for moveableStatement in self.gm.getMovables():
            # print(moveableStatement)
            self.gm.makeMove(moveableStatement)
            self.currentState.children.append(GameState(self.gm.getGameState(),currDepth + 1, moveableStatement))
            self.gm.reverseMove(moveableStatement)

        # for s in self.currentState.children:
        #     print(s.state)



        for idx,gs in enumerate(self.currentState.children):

            if gs not in self.visited.keys():
                # print("hello")
                self.gm.makeMove(gs.requiredMovable)

                self.currentState =  GameState(self.gm.getGameState(), currDepth + 1, gs.requiredMovable)
                self.currentState.parent = oldState
                self.visited[self.currentState] = True
                return False
                # self.requiredMovable = self.gm.getMovables()[idx]
                # hasNewNode = True

        # while !hasNewNode:
        #     self.gm.reverseMove(self.currentState.requiredMovable)
        ### Student code goes here
        return False


class SolverBFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Breadth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """
        ### Student code goes here
        return True
