class Sim:
    arr = []
    def __init__(self,id:int,name:str,balance:float,rps:float,circle:str):
        self.id = id
        self.name = name
        self.balance = balance
        self.rps = rps
        self.circle = circle
        Sim.arr.append(self)

class Solun:
    @classmethod
    def transferCircle(cls,arr,circle1:str,circle2:str):
        ans = []
        for i in arr:
            if i.circle.lower()==circle1.lower():
                i.circle = circle2
                ans.append(i)
        
        for i in range(len(ans)):
            for j in (range(len(ans)-i-1)):
                if ans[j].rps<ans[j+1].rps:
                    ans[j],ans[j+1] = ans[j+1],ans[j]
        
        return ans

for i in range(int(input("Enter number of test cases : "))):
    a = Sim(int(input("Enter Sim Id : ")),
            input("Enter Name : "),
            float(input("Enter Balance : ")),
            float(input("Enter Rate per Second : ")),
            input("Enter circle : "))

circle1 = input("\nEnter Circle 1 : ")
circle2 = input("Enter Circle 2 : ")

ans = Solun.transferCircle(Sim.arr,circle1,circle2)
for i in ans:
    print(i.id,i.name,i.circle,i.rps,sep=" ")

