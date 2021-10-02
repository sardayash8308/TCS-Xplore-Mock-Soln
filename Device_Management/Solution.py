class Phone:
    arr = []
    def __init__(self,phoneId:int,os:str,brand:str,price:int) -> None:
        self.phoneId = phoneId
        self.os = os
        self.brand = brand
        self.price = price
        Phone.arr.append(self)

class Solution:
    @classmethod
    def findPriceForGivenBrand(cls,arr,bra:str):
        ans=0
        for i in arr:
            if i.brand.lower()==bra.lower():
                ans+=i.price
        return ans
    
    @classmethod
    def getPhoneIdBasedOnOS(cls,arr,os:str)->Phone:
        for i in arr:
            if i.os.lower()==os.lower() and i.price>=50000:
                return i
        else:
            return None

for i in range(4):
    a = Phone(int(input("Enter Phone Id : ")),input("Enter Os"),input("Enter brand : "),int(input("Enter Price : ")))

bran = input("Enter Brand to check : ")
os = input("Enter Os to check : ")
priceAns = Solution.findPriceForGivenBrand(Phone.arr,bran)
if priceAns>0:  print(priceAns)
else:   print("The Given Brand is not available")

osAns = Solution.getPhoneIdBasedOnOS(Phone.arr,os)
if osAns==None: print("No phones are available with specified os and price range")
else:   print(osAns.phoneId)