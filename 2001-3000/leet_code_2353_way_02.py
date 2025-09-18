import heapq
from collections import defaultdict


class Food:
    def __init__(self, food, rating):
        self.food = food
        self.rating = rating

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.food < other.food
        return self.rating > other.rating


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_rating_dict = defaultdict(int)
        self.food_cuisine_dict = defaultdict(str)
        self.cuisine_food_dict = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_rating_dict[food] = rating
            self.food_cuisine_dict[food] = cuisine
            heapq.heappush(self.cuisine_food_dict[cuisine], Food(food, rating))

    def changeRating(self, food: str, newRating: int):
        self.food_rating_dict[food] = newRating
        heapq.heappush(self.cuisine_food_dict[self.food_cuisine_dict[food]], Food(food, newRating))

    def highestRated(self, cuisine: str) -> str:
        highest_rating = self.cuisine_food_dict[cuisine][0]

        while highest_rating.rating != self.food_rating_dict[highest_rating.food]:
            heapq.heappop(self.cuisine_food_dict[cuisine])
            highest_rating = self.cuisine_food_dict[cuisine][0]
        return highest_rating.food



b = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])

print(b.highestRated('japanese'))


