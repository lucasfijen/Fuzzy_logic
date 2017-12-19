"""
This database interaction function has been written by:
Lucas Fijen and Arie Soeteman
As part of an assignment for fuzzy logic at the University of Amsterdam
"""


import data as d

class Datainteraction:
    """ Interaction class for data between validation and training"""
    def __init__(self):
        """ Inits the datainteraction class, makes a validation and training
            set """
        self.val = d.Moviedata('valcomposers',
                               'valdirectors',
                               'valactors',
                               'valbusiness',
                               'valspecial-effects-companies',
                               'valratings')
        self.train = d.Moviedata('composers',
                                 'directors',
                                 'actors',
                                 'business',
                                 'special-effects-companies',
                                 'ratings')
        self.errorvalue = -1

    def actor_values(self, movie, ranging=0):
        """ returns average amount of movies starred by the actors,
            and the average ratings of these movies """
        actors = self.val.movie_actor(movie)
        results = []
        for actor in actors:
            movies = self.train.actor_movie(actor)
            if len(movies) == 0:
                continue
            avgrating = 0
            amount = 0
            for movie in movies:
                temprate = self.train.movie_rating(movie)
                if temprate >= 1:
                    avgrating += temprate
                    amount += 1
            if amount > 0:
                results.append((avgrating / amount, amount))

        if len(results) == 0:
            return self.errorvalue, self.errorvalue
        if ranging == 0 or ranging > len(results):
            ranging = len(results)
        amounts = [i[1] for i in results]
        amounts.sort(reverse=True)
        ratings = [i[0] for i in results]
        ratings.sort(reverse=True)
        rating = sum(ratings[:ranging]) / ranging
        amount = sum(amounts[:ranging]) / ranging
        return rating, amount

    def special_values(self, movie, ranging=0):
        """ returns average amount of movies done by special effect studio,
            and the average ratings of these movies """
        specials = self.val.movie_special(movie)
        results = []
        for special in specials:
            movies = self.train.special_movie(special)
            if len(movies) == 0:
                continue
            avgrating = 0
            amount = 0
            for movie in movies:
                temprate = self.train.movie_rating(movie)
                if temprate >= 1:
                    avgrating += temprate
                    amount += 1
            if amount > 0:
                results.append((avgrating / amount, amount))

        if len(results) == 0:
            return self.errorvalue, self.errorvalue
        if ranging == 0 or ranging > len(results):
            ranging = len(results)
        amounts = [i[1] for i in results]
        amounts.sort(reverse=True)
        ratings = [i[0] for i in results]
        ratings.sort(reverse=True)
        rating = sum(ratings[:ranging]) / ranging
        amount = sum(amounts[:ranging]) / ranging

        return rating, amount

    def director_values(self, movie, ranging=0):
        """ returns average amount of movies created by director
            and the average ratings of these movies """
        directors = self.val.movie_director(movie)
        results = []
        for director in directors:
            movies = self.train.director_movie(director)
            if len(movies) == 0:
                continue
            avgrating = 0
            amount = 0
            for movie in movies:
                temprate = self.train.movie_rating(movie)
                if temprate >= 1:
                    avgrating += temprate
                    amount += 1
            if amount > 0:
                results.append((avgrating / amount, amount))

        if len(results) == 0:
            return self.errorvalue, self.errorvalue
        if ranging == 0 or ranging > len(results):
            ranging = len(results)
        amounts = [i[1] for i in results]
        amounts.sort(reverse=True)
        ratings = [i[0] for i in results]
        ratings.sort(reverse=True)
        rating = sum(ratings[:ranging]) / ranging
        amount = sum(amounts[:ranging]) / ranging

        return rating, amount

    def composer_values(self, movie, ranging=0):
        """ returns average amount of movies with music created by composer
            and the average ratings of these movies """
        composers = self.val.movie_composer(movie)
        results = []
        for composer in composers:
            movies = self.train.composer_movie(composer)
            if len(movies) == 0:
                continue
            avgrating = 0
            amount = 0
            for movie in movies:
                temprate = self.train.movie_rating(movie)
                if temprate >= 1:
                    avgrating += temprate
                    amount += 1
            if amount > 0:
                results.append((avgrating / amount, amount))

        if len(results) == 0:
            return self.errorvalue, self.errorvalue
        if ranging == 0 or ranging > len(results):
            ranging = len(results)
        amounts = [i[1] for i in results]
        amounts.sort(reverse=True)
        ratings = [i[0] for i in results]
        ratings.sort(reverse=True)
        rating = sum(ratings[:ranging]) / ranging
        amount = sum(amounts[:ranging]) / ranging

        return rating, amount

    def get_budget(self, movie):
        """ returns budget of a movie in milions"""
        budget = self.val.movie_budget(movie)
        return budget

    def get_rating(self, movie):
        """ returns the rating of a movie """
        return self.val.movie_rating(movie)

    def get_all_movies(self):
        """ returns all movies that appear in the validation data """
        return self.val.get_movies()

#datainter = Datainteraction()
#print(datainter.special_values('Avengers: Age of Ultron', ranging=3))
#print(datainter.get_budget('Avengers: Age of Ultron'))
