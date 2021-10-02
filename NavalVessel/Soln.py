class NavalVessel:
    arr = []
    def __init__(self,id:int,name:str,novp:int,novc:int,purpose:str):
        self.vesselId = id
        self.vesselNAme = name
        self.noOfVoyagesPlanned = novp
        self.noOfVoyagesCompleted = novc
        self.purpose = purpose
        self.percentage = novc/novp * 100
        self.classification = None
        self.setClass()
        NavalVessel.arr.append(self)
    def setClass(self):
        if self.percentage==100:    self.classification="Star"
        elif self.percentage<=99 and self.percentage>=80:   self.classification="Leader"
        elif self.percentage<=79 and self.percentage>=55:   self.classification="Inspirer"
        else:   self.classification = "Striver"

class Soln:
    @classmethod
    def findAvgVoyagesByPct(cls,arr,percentage:int):
        c = 0 #counter for no of voygaes
        total = 0
        for i in arr:
            if (i.percentage >= percentage):
                total += i.noOfVoyagesCompleted
                c+=1
        if c>0: return total//c
        else:   return 0

    @classmethod
    def findVesselByGrade(cls,arr,purpose:str)->NavalVessel:
        for i in arr:
            if i.purpose.lower()==purpose.lower():
                return i
        else:   return None 

n = int(input("Number of Test cases : "))

for i in range(n):
    a = NavalVessel(int(input("Enter Vessel Id : ")),
            input("Enter Vessel Name : "),
            int(input("Enter No of Voyages Planned : ")),
            int(input("Enter no of Voyages Completed : ")),
            input("Enter Purpose : "))

ans = Soln.findAvgVoyagesByPct(NavalVessel.arr,int(input("\nEnter Percentaeg value : ")))
ans2 = Soln.findVesselByGrade(NavalVessel.arr,input("Enter Purpose : "))

print(ans)
if ans2!=None:  print(ans2.vesselNAme + "%" + ans2.classification)
else:   print("No Naval Vessel is available with the specified purpose")
