from typing import Counter


class Movie:
    arr = []
    def __init__(self,id:int,director:str,rating:int,budget:int) -> None:
        self.movieId = id
        self.director = director
        self.budget = budget
        self.rating = rating
        Movie.arr.append(self)
    
class Soln:
    @classmethod
    def findAvgBudgetByDirector(cls,arr,director:str):
        c = 0 # counter to count the no of movies by director
        tb = 0 #Total budget of director
        for i in arr:
            if i.director.lower()==director.lower():
                tb+=i.budget
                c+=1
        if c>0: return tb//c
        else:   return 0
    
    @classmethod
    def getMovieRatingByBudget(cls,arr,rating,budget)->Movie:
        for i in arr:
            if(i.rating==rating and i.budget==budget) and(budget%rating==0):
                return i
        else:
            return None

n = int(input("Number of test cases to be passed : "))
for i in range(n):
    a = Movie(int(input("Enter Movie Id : ")),
            input("Enter Director Name of above Movie : "),
            int(input("Enter Rating for Movie : ")),
            int(input("Enter Budget For Movie : ")))

avgBu = Soln.findAvgBudgetByDirector(Movie.arr,
        input("\nEnter Director Name : "))
ans2 =  Soln.getMovieRatingByBudget(Movie.arr,
        int(input("Enter Rating to check : ")),
        int(input("Enter Budget to check : ")))

if avgBu>0: print(avgBu)
else:   print("Sorry - The given director has not yet directed any movie")

if ans2==None:
    print("Soory - No Movie is available with the apecified rating and budget requirement")
else:
    print(ans2.movieId)
