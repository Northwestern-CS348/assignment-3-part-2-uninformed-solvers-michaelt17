
from solver import *
from queue import *

bfsQueue = Queue()

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

        if self.currentState.state == self.victoryCondition:
            return True

        # print(self.currentState.state)

        currDepth = self.currentState.depth
        oldState = self.currentState

        # print (self.gm.getMovables())
        for moveableStatement in self.gm.getMovables():
            # print(moveableStatement)
            self.gm.makeMove(moveableStatement)
            self.currentState.children.append(GameState(self.gm.getGameState(),currDepth + 1, moveableStatement))
            self.gm.reverseMove(moveableStatement)

        # for s in self.currentState.children:
        #     print(s.state)



        for gs in self.currentState.children:

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

        if self.currentState.state == self.victoryCondition:
            return True



        currDepth = self.currentState.depth
        oldState = self.currentState
        #
        print("current state: " + str(self.currentState.state))
        print("new movables")

        for moveableStatement in self.gm.getMovables():
            print(moveableStatement)
            self.gm.makeMove(moveableStatement)
            self.currentState.children.append(GameState(self.gm.getGameState(),currDepth + 1, moveableStatement))
            self.gm.reverseMove(moveableStatement)


        for gs in self.currentState.children:
            gs.parent = oldState
            print(gs.state)
            if gs not in self.visited.keys():
                print("putting in queue")
                bfsQueue.put(gs)
                self.visited[gs] = True

        newGameState =  bfsQueue.get()

        notTrue = True

        while notTrue:
            if newGameState not in self.visited.keys():
                self.gm.makeMove(gs.requiredMovable)
                self.currentState =  GameState(self.gm.getGameState(), currDepth + 1, gs.requiredMovable)
                notTrue = False
            else:
                if not bfsQueue.empty():
                    newGameState = bfsQueue.get()

        # self.visited[self.currentState] = True
        return False
        # newGameState = bfsQueue.get()
        # self.gm.makeMove(newGameState.requiredMovable)
        # self.currentState = newGameState

        # if newGameState not in self.visited.keys():
        #     self.gm.makeMove(newGameState.requiredMovable)
        #     self.currentState =  newGameState
        #     self.visited[self.currentState] = True
        #     return False
