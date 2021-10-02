class Associate:
    def __init__(self,id,name,tech,xperienxe):
        self.id = id
        self.name = name
        self.technology = tech
        self.experienceInYears = xperienxe
        

class Solution:
    @classmethod
    def associatesForGivenTechnology(cls,arrayOfAssociates,searchTech):
        l = []
        for i in arrayOfAssociates:
            if (i.technology.lower() == searchTech.lower()) and (i.experienceInYears%5==0):
                l.append(i.id)
        return l

arr = []
for i in range(1):
    id = int(input("Enter Id : "))
    name = input("Enter NAme : ")
    tech = input("Technology : ")
    xperience = int(input("Experience in Years : "))
    a = Associate(id,name,tech,xperience)
    arr.append(a)

tech = input("Enter technology to search : ")
l = Solution.associatesForGivenTechnology(arr,tech)
for i in l: print(i)
