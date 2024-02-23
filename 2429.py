from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ftoc = {}
        self.ftor = {}
        self.c = defaultdict(SortedList)
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.ftoc[f] = c
            self.ftor[f] = r
            self.c[c].add((r, f))
        
        

    def changeRating(self, food: str, newRating: int) -> None:
        oldR = self.ftor[food]
        oldC = self.ftoc[food]
        
        self.c[oldC].remove((oldR, food))
        self.c[oldC].add((newRating, food))
        self.ftor[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        #print(self.c, cuisine)
        high = self.c[cuisine][-1][0]
        for r, f in self.c[cuisine]:
            if r == high:
                return f
        return None
            


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)