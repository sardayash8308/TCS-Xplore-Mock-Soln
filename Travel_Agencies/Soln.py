class TravelAgencies:
    arr = []
    def __init__(self,regno:int,name:str,pkgType:str,price:int,flightFacility:str):
        self.regNo = regno
        self.agencyName = name
        self.packageType = pkgType
        self.price = price
        if flightFacility.lower().lstrip() == 'true':    self.flightFacility = True
        else:   self.flightFacility = False
        TravelAgencies.arr.append(self)
    
class Soln:
    @classmethod
    def findAgencyWithHighestPackagePrice(cls,arr):
        ans = 0
        for i in arr:
            if i.price>ans: ans = i.price
        return ans
    
    @classmethod
    def agencyDetailsForGivenldAndType(cls,arr,regno:int,pkgtype:str)->TravelAgencies:
        for i in arr:
            #print(i.flightFacility,i.agencyName,i.price,i.packageType,sep="->")
            if (i.flightFacility==True) and (i.regNo == regno) and(i.packageType.lower()==pkgtype.lower()):
               print(i.agencyName,i.price,sep=":")


n = int(input("Test cases : "))
for i in range(n):
    a = TravelAgencies(int(input("Enter Reg No : ")),
                input("Enter Travel agency Name : "),
                input("Enter Package Type : "),
                int(input("Enter Price : ")),
                input("Enter Fligtht Availability : "))


regno = int(input("Enter Reg No : "))
pkgt = input("Enter Package Type : ")

print(Soln.findAgencyWithHighestPackagePrice(TravelAgencies.arr))

Soln.agencyDetailsForGivenldAndType(TravelAgencies.arr,regno,pkgt)