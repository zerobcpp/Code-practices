from sortedcontainers import SortedList

class FoodItem:
    def __init__(self, f, r):
        self.food = f
        self.rating = r
    
    def __lt__(self, other):
        if self.rating == other.rating:
            return self.food < other.food
        return self.rating < other.rating
    
    def __str__(self):
        return f'{self.food}, {self.rating}'
    
    
class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.ftoc = {}
        self.ftor = {}
        self.c = defaultdict(list)
        
        for f, c, r in zip(foods, cuisines, ratings):
            heappush(self.c[c], FoodItem(f, -r))
            self.ftoc[f] = c
            self.ftor[f] = r
        
    def changeRating(self, food, rating):
        c = self.ftoc[food]
        self.ftor[food] = rating
        heappush(self.c[c], FoodItem(food, -rating))
    
    def highestRated(self, cuisine):
        item = self.c[cuisine][0]
        right_rating = self.ftor[item.food]

        while -right_rating != item.rating:
            
            heappop(self.c[cuisine])
            item = self.c[cuisine][0]
            right_rating = self.ftor[item.food]
        
        return item.food

class FoodRatingsMap:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ftoc = {}
        self.ftor = {}
        self.c = defaultdict(SortedList)
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.ftoc[f] = c
            self.ftor[f] = r
            self.c[c].add((-r, f))
        
        

    def changeRating(self, food: str, newRating: int) -> None:
        oldR = self.ftor[food]
        oldC = self.ftoc[food]
        
        self.c[oldC].remove((-oldR, food))
        self.c[oldC].add((-newRating, food))
        self.ftor[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        return self.c[cuisine][0][1]    


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)