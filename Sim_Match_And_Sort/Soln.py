from typing import ClassVar


class Sim:
    arr = []
    def __init__(self,id:int,company:str,balance:int,rps:float,circle:str):
        self.id = id
        self.company = company
        self.balance = balance
        self.ratePerSecond = rps
        self.circle = circle
        Sim.arr.append(self)

class Solution:
    @classmethod
    def matchAndSort(cls,arr,search_circle:str,search_rate:float):
        ans = []
        for i in arr:
            if (i.circle.lower()==search_circle.lower()) and (search_rate>i.ratePerSecond):
                ans.append(i)
        for i in range(len(ans)):
            for j in range(len(ans)-i-1):
                if ans[j].balance<ans[j+1].balance:
                    ans[j],ans[j+1] = ans[j+1],ans[j]

        return ans
    
n = int(input("Number of test cases : "))
for i in range(n):
    a = Sim(int(input("Enter Id : ")),
            input("Enter Company Name : "),
            int(input("Enter Balance : ")),
            float(input("Enter Rate per Second : ")),
            input("Enter Circle : "))

ans = Solution.matchAndSort(Sim.arr,
            input("\nEnter Search Circle"),
            float(input("Enter Search Rate")))

for i in ans:
    print(i.id)