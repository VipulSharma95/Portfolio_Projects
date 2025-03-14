class Game:

    def __init__(self):
        self.score=0

    def roll(self,numOfRolls,pins):
        for roll in range(numOfRolls):
            self.score+=pins