import random






class App:
    def __init__(self):
        pass
    def StartGame(self):
        self.PoneScore = 0
        self.PtwoScore = 0
        self.rolltimes = 0
        self.maxrolls = int(input("enter a rolls times"))
        print("Starting")
        self.poneroll = Dice()
        self.ptworoll = Dice()
        while self.rolltimes <= self.maxrolls:
            self.rolltimes += 1
            self.poneroll.Roll()
            self.ptworoll.Roll()
            self.RollCheck()
        print(self.ShowGameStats())
        with open("game-results.txt","w") as result:
            result.write(self.ShowGameStats())
    def RollCheck(self):
        if self.poneroll.rollnumber < self.ptworoll.rollnumber:
            print("player one wins")
            self.PoneScore += 1
        elif self.poneroll.rollnumber > self.ptworoll.rollnumber:
            print("player two winds ")
            self.PtwoScore += 1
        else:
            print("the roll was a draw")

    def ShowGameStats(self):
        scoreboard = f"""
            diceroller score board
            ---------------------
        player one            player two
        __________            _________
        {self.PoneScore}                     {self.PtwoScore}  
        """
        return scoreboard


class Dice:
    def __init__(self):
        self.rolls = 0
        self.rollnumbers = []
        self.rollnumber = 0;
    def Roll(self):
        self.rollnumber = random.randint(1,10)
        self.rollnumbers.append(self.rollnumber)



app = App()
app.StartGame()