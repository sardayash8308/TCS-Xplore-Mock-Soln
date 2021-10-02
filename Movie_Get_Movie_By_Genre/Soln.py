class Movie:
    arr = []
    def __init__(self,movieName:str,company:str,genre:str,budget:int) -> None:
        self.movieName = movieName
        self.company = company
        self.genre = genre
        self.budget = budget
        Movie.arr.append(self)

class Soln:
    @classmethod
    def getMovieByGenre(cls,arr,genre:str):
        ans = []
        for i in arr:
            if i.genre.lower() == genre.lower():
                ans.append(i)
        return ans
    
n = int(input("Number of Test Cases : "))
for i in range(n):
    a = Movie(input("Enter Movie Name : "),
        input("Enter Movie Company : "),
        input("Enter Movie genre : "),
        int(input("Enter Movie Budget : ")))

ans = Soln.getMovieByGenre(Movie.arr,input("\nEnter Genre to search : "))

if len(ans)>0:
    for i in ans:
        if i.budget>80000000:   print("High Budget Movie")
        else:   print("Low Budget Movie")
