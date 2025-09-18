# Time Limit Exceeded
# Time Limit Exceeded
# Time Limit Exceeded


class FoodRatings:
    # def __init__(self):
    #     self.ratings_dict = None
    #     self.ratings = list(int)
    #     self.cuisines = list(str)
    #     self.foods = list(str)

    def __init__(self, foods: list[str] = [], cuisines: list[str] = [], ratings: list[int]= []):
        self.ratings = ratings
        self.cuisines = cuisines
        self.foods = foods
        self.ratings_dict = dict(zip(foods, ratings))

    def FoodRatings(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.ratings = ratings
        self.cuisines = cuisines
        self.foods = foods
        # self.ratings_dict = dict(zip(foods, ratings))

    def changeRating(self, food: str, newRating: int):
        index_food = self.foods.index(food)
        self.ratings[index_food] = newRating
        # self.ratings_dict[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        highest_rating = -1
        result = ''
        for i, food_cuisine in enumerate(self.cuisines):
            if food_cuisine == cuisine:
                if self.ratings[i] > highest_rating:
                    highest_rating = self.ratings[i]
                    result = self.foods[i]
                elif self.ratings[i] == highest_rating:
                    result = min(result, self.foods[i])

        return result



a = FoodRatings()


b = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
