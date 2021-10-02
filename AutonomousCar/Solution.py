class AutonomousCar:
    a = []
    def __init__(self,id,brand,testCond,testPass,enviornment) -> None:
        self.carId = id
        self.brand = brand
        self.testConducted = testCond
        self.noOfTestPassed = testPass
        self.enviornment  = enviornment
        self.grade = (self.noOfTestPassed / self.testConducted) * 100
        AutonomousCar.a.append(self)


class Solution:
    @classmethod
    def findTestPassedByEnv(cls,arr:list,env:str):
        ans = 0
        for i in arr:
            if i.enviornment.lower() == env.lower():    ans+=i.noOfTestPassed
        return ans

    @classmethod
    def updateCarGrade(cls,bra:str,arr)->float:
        for i in arr:
            if i.brand.lower() == bra.lower():
                if i.grade>=80: print(f"{i.brand}::A1")
                else:   print(f"{i.brand}::B2")
        else:
            print("No Car is available with the specified brand")

for i in range(4):
    car = AutonomousCar(int(input("Car Id : ")),
          input("CAr brand : "),
          int(input("Test Conducted : ")),
          int(input("Test Passed : ")),
          input("Enviornment : "))

env = input("Enviornment to check : ")
bra = input("Brand to check : ")

ans = Solution.findTestPassedByEnv(AutonomousCar.a,env)
print(ans)
Solution.updateCarGrade(bra,AutonomousCar.a)
