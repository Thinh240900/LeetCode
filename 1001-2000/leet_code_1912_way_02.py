import heapq
from collections import defaultdict


class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.rented = set()
        self.movies = defaultdict(list)
        self.prices = defaultdict(int)
        for shop, movie, price in entries:
            self.movies[movie].append((price, shop))
            self.prices[(shop, movie)] = price

        for movie in self.movies.values():
            movie.sort()

    def search(self, movie: int) -> list[int]:
        arr = []
        for price, shop in self.movies[movie]:
            if (shop, movie) not in self.rented:
                arr.append(shop)
                if len(arr) == 5:
                    return arr
        return arr

    def rent(self, shop: int, movie: int):
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int):
        self.rented.remove((shop, movie))

    def report(self) -> list[list[int]]:
        arr = []
        for shop, movie in self.rented:
            arr.append([self.prices[(shop, movie)], shop, movie])
        arr.sort()
        return [[shop, movie] for _, shop, movie in arr[:5]]


a = MovieRentingSystem(3,  [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
print(a.search(1))
a.rent(0, 1)
a.rent(1, 2)
print(a.report())
a.drop(1, 2)
print(a.search(2))