class Inventory:
    arr = []
    def __init__(self,id:int,maxQuant:int,currentQuant:int,threshold:int):
        self.inventoryId = id
        self.maximumQuantity = maxQuant
        self.currentQuantity = currentQuant
        self.threshold = threshold
        Inventory.arr.append(self)
    
class Solution:
    @classmethod
    def replenish(cls,arr,limit:int):
        ans = []
        for i in arr:
            if i.threshold<=limit:
                ans.append(i)
        return ans

n = int(input("Number of test cases to be runned : "))
for i in range(n):
    a = Inventory(int(input("Enter Inventory Id : ")),
        int(input("Enter Maximum Quantity : ")),
        int(input("Enter Current Quantity : ")),
        int(input("Enter Threshold : ")))

limit = int(input("Enter Limit : "))
ans = Solution.replenish(Inventory.arr,limit)
for i in ans:
    print(i.inventoryId,end="")
    if i.threshold>=75: print(" Critical Filling")
    elif i.threshold>=50 and i.threshold<75:    print(" Moderate Filling")
    else:   print(" Non-Critical Filling")
