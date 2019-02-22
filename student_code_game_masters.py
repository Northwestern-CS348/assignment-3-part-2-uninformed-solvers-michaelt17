from game_master import GameMaster
from read import *
from util import *

class TowerOfHanoiGame(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        """
        See overridden parent class method for more information.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?disk ?init ?target)')

    def getGameState(self):
        """
        Returns a representation of the game in the current state.
        The output should be a Tuple of three Tuples. Each inner tuple should
        represent a peg, and its content the disks on the peg. Disks
        should be represented by integers, with the smallest disk
        represented by 1, and the second smallest 2, etc.

        Within each inner Tuple, the integers should be sorted in ascending order,
        indicating the smallest disk stacked on top of the larger ones.

        For example, the output should adopt the following format:
        ((1,2,5),(),(3, 4))

        Returns:
            A Tuple of Tuples that represent the game state
        """

        tuple1 = ()
        tuple2 = ()
        tuple3 = ()

        t1Holder = []
        t2Holder = []
        t3Holder = []
        for fact in self.kb.facts:
            # print(fact.statement.predicate)
            if fact.statement.predicate == 'on':
                # print(fact.statement.terms[1])
                diskNum = int(str(fact.statement.terms[0])[4])
                pegNum = int(str(fact.statement.terms[1])[3])

                if pegNum == 1:
                    t1Holder.append(diskNum)
                    # tuple1 += (diskNum,)
                elif pegNum == 2:
                    t2Holder.append(diskNum)
                    # tuple2 += (diskNum,)
                else:
                    t3Holder.append(diskNum)
                    # tuple3 += (diskNum,)

        t1Holder.sort()
        t2Holder.sort()
        t3Holder.sort()

        for item in t1Holder:
            tuple1 += (item,)
        for item2 in t2Holder:
            tuple2 += (item2,)
        for item3 in t3Holder:
            tuple3 += (item3,)

        return (tuple1,tuple2,tuple3)

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable disk1 peg1 peg3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        # I forgot about kb_ask until I finished this. So I might go back and change if I have time
        movingDisk = movable_statement.terms[0]
        fromPeg = movable_statement.terms[1]
        destPeg = movable_statement.terms[2]

        factsToAdd = []
        factsToRetract = []

        # 4 facts you'll need to add/retract no matter what: disk on new peg/disk off of old peg,
        # and removing the old top and adding the new top
        addStatementOn = Statement(["on", movingDisk, destPeg])
        # print(addStatement)
        removeStatementOn = Statement(["on", movingDisk, fromPeg])
        # print(removeStatement)
        addStatementTop = Statement(["top", movingDisk,destPeg])
        removeStatementTop = Statement(["top", movingDisk,fromPeg])

        factsToAdd.append(Fact(addStatementOn))
        factsToAdd.append(Fact(addStatementTop))

        factsToRetract.append(Fact(removeStatementOn))
        factsToRetract.append(Fact(removeStatementTop))

        if Fact(Statement(["empty", destPeg])) in self.kb.facts:
            factsToRetract.append(Fact(Statement(["empty", destPeg])))
            factsToAdd.append(Fact(Statement(["onTop",movingDisk,"table"])))
        else:
            # print("in first else")
            for fact in self.kb.facts:
                if fact.statement.predicate == "top":
                    if fact.statement.terms[1] == destPeg:
                        oldTopDisk = fact.statement.terms[0]

                        factsToAdd.append(Fact(Statement(["onTop",movingDisk,oldTopDisk])))
                        factsToRetract.append(Fact(Statement(["top",oldTopDisk,destPeg])))
            # bindings = match()

            # factsToAdd.append(Fact(Statement(["onTop",])))
            # find disk on top of destPeg and add onTop

        if Fact(Statement(["onTop", movingDisk, "table"])) in self.kb.facts:
            factsToAdd.append(Fact(Statement(["empty", fromPeg])))
            factsToRetract.append(Fact(Statement(["onTop",movingDisk,"table"])))
        else:
            # print("in second else")
            for fact in self.kb.facts:
                if fact.statement.predicate == "onTop":
                    if fact.statement.terms[0] == movingDisk:
                        newTopDisk = fact.statement.terms[1]
                        factsToAdd.append(Fact(Statement(["top",newTopDisk,fromPeg])))
                        factsToRetract.append(Fact(Statement(["onTop",movingDisk,newTopDisk])))
            # find disk below movingDisk and add top

        # print(factsToAdd)
        # print(factsToRetract)

        factsToRetract.append(Fact(movable_statement))

        for retractFact in factsToRetract:
            self.kb.kb_retract(retractFact)

        for addFact in factsToAdd:
            self.kb.kb_assert(addFact)



    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[2], sl[1]]
        self.makeMove(Statement(newList))

class Puzzle8Game(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        """
        Create the Fact object that could be used to query
        the KB of the presently available moves. This function
        is called once per game.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?piece ?initX ?initY ?targetX ?targetY)')

    def getGameState(self):
        """
        Returns a representation of the the game board in the current state.
        The output should be a Tuple of Three Tuples. Each inner tuple should
        represent a row of tiles on the board. Each tile should be represented
        with an integer; the empty space should be represented with -1.

        For example, the output should adopt the following format:
        ((1, 2, 3), (4, 5, 6), (7, 8, -1))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### Student code goes here
        pass

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable tile3 pos1 pos3 pos2 pos3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        pass

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[3], sl[4], sl[1], sl[2]]
        self.makeMove(Statement(newList))
