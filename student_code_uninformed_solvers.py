
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
        # print()
        # print("current state: " + str(self.currentState.state))
        # print("new movables")

        if bfsQueue.empty():
            # print("queue was empty")
            for moveableStatement in self.gm.getMovables():
                # print(moveableStatement)
                self.gm.makeMove(moveableStatement)
                newGameState = GameState(self.gm.getGameState(),currDepth + 1, moveableStatement)
                newGameState.parent = oldState
                self.currentState.children.append(newGameState)
                self.gm.reverseMove(moveableStatement)

            for gs in self.currentState.children:
                # print("new states")
                # print(gs.state)
                # print(gs.parent.state)
                bfsQueue.put(gs)
                self.visited[gs] = True
        else:
            # print("queue was not empty")
            newState = bfsQueue.get()
            # print("new state state")
            # print(newState.state)
            # print(self.victoryCondition)
            # print(newState.parent.state)



            movableList = []
            currState = newState
            while currState.parent is not None:
                # print("woooo")
                movableList.append(currState.requiredMovable)
                currState = currState.parent
            # print(movableList)

            for m in movableList[::-1]:
                self.gm.makeMove(m)

            if newState.state == self.victoryCondition:
                # print("I won the game!!!")
                bfsQueue.queue.clear()
                return True
            else:
                self.currentState = newState
                for moveableStatement in self.gm.getMovables():
                    # print(moveableStatement)
                    self.gm.makeMove(moveableStatement)
                    newGameState = GameState(self.gm.getGameState(),currDepth + 1, moveableStatement)
                    newGameState.parent = newState
                    newState.children.append(newGameState)
                    self.gm.reverseMove(moveableStatement)
                for gs in newState.children:
                    # print("second new states")
                    # print(gs.state)
                    # print(gs.parent.state)
                    if gs not in self.visited.keys():
                        bfsQueue.put(gs)
                        self.visited[gs] = True
                for m2 in movableList:
                    self.gm.reverseMove(m2)
                return False

        # while self.currentState !=

        return False
