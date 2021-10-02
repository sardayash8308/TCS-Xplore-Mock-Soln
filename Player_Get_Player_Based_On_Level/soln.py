class Player:
    arr = []
    def __init__(self,id:int,skill:str,level:str,points:int):
        self.playerId = id
        self.skill = skill
        self.level = level
        self.points = points
        Player.arr.append(self)

class Solution:
    @classmethod
    def findPointsForGivenSkill(cls,arr,skill:str):
        ans = 0
        for i in arr:
            if i.skill.lower()==skill.lower():
                ans+=i.points
        return ans

    @classmethod
    def getPlayerBasedOnLevel(cls,arr,level:str,skill:str)->Player:
        for i in arr:
            if (i.skill.lower() == skill.lower()) and(i.level.lower()==level.lower())and i.points>=20:
                return i
        else:   return None

n = int(input("Number of Test Cases : "))
for i in range(n):
    a = Player(int(input("Enter Player Id : ")),
                input("Enter Player Skill"),
                input("Enter Player Level : "),
                int(input("Enter Player Points : ")))
skill = input("\nEnter required Skill : ")
ans1 = Solution.findPointsForGivenSkill(Player.arr,skill)
                
ans2 = Solution.getPlayerBasedOnLevel(Player.arr,input("Enter required Level : "),skill)
                
if ans1>0:  print(ans1)
else:   print("The given Skill is not available")

if ans2==None:  print("No player is available with specified level, skill and eligibility points")
else:   print(ans2.playerId)
