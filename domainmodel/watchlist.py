from domainmodel.movie import Movie

class WatchList:

    def __init__(self):
        self.__watch_list = []
        self.__current = -1;


    def add_movie(self, movie):
        if movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie):
        if movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if index < len(self.__watch_list):
            return self.__watch_list[index]
        else:
            return None

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if self.size() > 0:
            return self.size()
        else:
            return None

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__current < self.size()):
            self.__current += 1
            return self.__watch_list[self.__current]
        else:
            raise StopIteration




wl = WatchList()
m1 = Movie("007", 2010)
m2 = Movie("Star Wars", 2010)
m3 = Movie("Generic Movie", 2019)
wl.add_movie(m1)
wl.add_movie(m2)
print(wl.size())
wl.add_movie(m2)
print(wl.size())
wl.remove_movie(m1)
print(wl.size())
wl.remove_movie(m3)
print(wl.size())
wl.select_movie_to_watch(1)
wl.select_movie_to_watch(0)

wl = WatchList()

wl.add_movie(m1)
wl.add_movie(m2)
wl.add_movie(m3)
for movie in wl:
    print(movie)


