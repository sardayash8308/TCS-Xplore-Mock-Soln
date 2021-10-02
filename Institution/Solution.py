class Institution:
    arr = []
    def __init__(self,iid,iiname,nosp,nosc,location) -> None:
        self.institutionId = iid
        self.institutionName = iiname
        self.noOfStudentsPlaced = nosp
        self.noOfStudentsCleared = nosc
        self.location = location
        self.grade = (nosp/nosc)*100
        Institution.arr.append(self)

class Solution:
    @classmethod
    def findNumClearanceByLoc(cls,arr,loc:str):
        ans = 0
        for i in arr:
            if i.location.lower() == loc.lower():
                ans += i.noOfStudentsCleared
        return ans
    
    @classmethod
    def updateInstitutionGrade(cls,name:str,arr)->Institution:
        for i in arr:
            if i.institutionName.lower()==name.lower():
                return i
        else:   return None
    

n = int(input("No of test cases to be passed : "))
for i in range(n):
    a = Institution(int(input("Enter Instituition Id : ")),input("Enter Institution Name : "),
    int(input("Enter no of Students Placed : ")),int(input("Enter No Of Students Cleared : ")),
    input("Enter Institute Location : "))


loc = input("\nEnter Location to check : ")
iname = input("Enter Instituition NAme to Check : ")

ans = Solution.findNumClearanceByLoc(Institution.arr,loc)
if ans>0:   print(ans)
else:   print("There are no cleared students in this particular location")

insti = Solution.updateInstitutionGrade(iname,Institution.arr)
if insti==None: print("No Institute is available with the specified name")
else:
    print(f"{insti.institutionName}::",end="")
    if insti.grade>=80: print("A")
    else:   print("B")
    