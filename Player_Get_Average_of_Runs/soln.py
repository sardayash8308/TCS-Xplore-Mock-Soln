class Player:
    arr = []
    def __init__(self,id:int,name:str,iccRank:int,matchesPlayed:int,runsScored:int):
        self.id = id
        self.name = name
        self.iccRank = iccRank
        self.matchesPlayed = matchesPlayed
        self.runsScored = runsScored
        self.avg = self.runsScored//self.matchesPlayed
        Player.arr.append(self)

class Solution:
    @classmethod
    def findAverageOfRuns(cls,arr,target:int):
        ans = []
        for i in arr:
            if i.matchesPlayed>=target: ans.append(i)
        return ans

n = int(input("Number of test Cases : "))
for i in range(n):
    a = Player(int(input("Enter Player Id : ")),
            input("Enter Player Name : "),
            int(input("Enter player Icc Rank")),
            int(input("Enter MAtches Played : ")),
            int(input("Enter Runs Scored")))

ans = Solution.findAverageOfRuns(Player.arr,int(input("\nEnter Target : ")))
for i in ans:
    if i.avg>=80 and i.avg<=100: print("Grade A")
    elif i.avg>=50 and i.avg<79:   print("Grade B")
    else:   print("Grade C")


