class Medicine:
    arr = []
    def __init__(self,name:str,batch:str,disease:str,price:int) -> None:
        self.name = name
        self.batch =batch
        self.disease=disease
        self.price = price
        Medicine.arr.append(self)

class Soln:
    @classmethod
    def getPriceByDisease(cls,arr,disease:str):
        ans = []
        for i in arr:
            if i.disease.lower() == disease.lower():
                ans.append(i.price)
                #print(i.disease)
        return sorted(ans)

n = input("Enter no. of terst cases : ")
for i in range(int(n)):
    a = Medicine(input("Enter Medicine Name : "),
                input("Enter Medicine Batch : "),
                input("Enter Medicine disease : "),
                input("Enter Medicine Price : "))

ans = Soln.getPriceByDisease(Medicine.arr,input("\nEnter Disease name : "))
for i in ans:   print(i)
    
