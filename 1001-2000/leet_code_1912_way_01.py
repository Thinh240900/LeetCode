import heapq
from collections import defaultdict


class Movie:
    def __init__(self, shop, movie, price):
        self.shop = shop
        self.movie = movie
        self.price = price

    def __lt__(self, other):
        if self.price == other.price:
            if self.shop == other.shop:
                return self.movie < other.movie
            return self.shop < other.shop
        return self.price < other.price

    def __eq__(self, other):
        return self.shop == other.shop and self.movie == other.movie and self.price == other.price

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.n = n
        self.rented = []
        self.movies = defaultdict(list)
        self.check_price = defaultdict(int)
        for shop, movie, price in entries:
            a  = Movie(shop, movie, price)
            self.movies[movie].append(a)
            self.check_price[(shop, movie)] = price

        for movie in self.movies.values():
            movie.sort()

    def search(self, movie: int) -> list[int]:
        arr = []
        for data in self.movies[movie]:
            if data not in self.rented:
                arr.append(data.shop)
                if len(arr) == 5:
                    return arr
        return arr

    def rent(self, shop: int, movie: int):
        self.rented.append(Movie(shop, movie, self.check_price[(shop, movie)]))

    def drop(self, shop: int, movie: int):
        self.rented.remove(Movie(shop, movie, self.check_price[(shop, movie)]))

    def report(self) -> list[list[int]]:
        arr = []
        self.rented.sort()  # sort rented movies by price, shop, movie
        for item in self.rented[:5]:
            arr.append([item.shop, item.movie])
        return arr


a = MovieRentingSystem(3,  [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
print(a.search(1))
a.rent(0, 1)
a.rent(1, 2)
print(a.report())
a.drop(1, 2)
print(a.search(2))