#import numpy as np
import data as d

class Datainteraction:
    """ Interaction class for data between validation and training"""
    def __init__(self):
        """ Inits the datainteraction class, makes a validation and training set """
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

    def actor_values(self, movie):
        """ returns average amount of movies starred by the actors,
            and the average ratings of these movies """
        actors = self.val.movie_actor(movie)
        amount = 0
        rating = 0
        length = len(actors)
        for actor in actors:
            movies = self.train.actor_movie(actor)
            if len(movies) == 0:
                length -= 1
                continue
            amount += len(movies)
            avgrating = 0
            for mov in movies:
                avgrating += self.train.movie_rating(mov)
            rating += avgrating / len(movies)
        if length == 0:
            return 0, self.errorvalue
        amount /= length
        rating /= length
        return amount, rating

    def special_values(self, movie):
        """ returns average amount of movies done by special effect studio,
            and the average ratings of these movies """
        specials = self.val.movie_special(movie)
        amount = 0
        rating = 0
        length = len(specials)
        for spec in specials:
            movies = self.train.special_movie(spec)
            if len(movies) == 0:
                length -= 1
                continue
            amount += len(movies)
            avgrating = 0
            for mov in movies:
                avgrating += self.train.movie_rating(mov)
            rating += avgrating / len(movies)
        if length == 0:
            return 0, self.errorvalue
        amount /= length
        rating /= length
        return amount, rating

    def director_values(self, movie):
        """ returns average amount of movies created by director
            and the average ratings of these movies """
        directors = self.val.movie_director(movie)
        amount = 0
        rating = 0
        length = len(directors)
        for direc in directors:
            movies = self.train.director_movie(direc)
            if len(movies) == 0:
                length -= 1
                continue
            amount += len(movies)
            avgrating = 0
            for mov in movies:
                avgrating += self.train.movie_rating(mov)
            rating += avgrating / len(movies)
        if length == 0:
            return 0, self.errorvalue
        amount /= len(directors)
        rating /= len(directors)
        return amount, rating

    def composer_values(self, movie):
        """ returns average amount of movies with music created by composer
            and the average ratings of these movies """
        composers = self.val.movie_composer(movie)
        amount = 0
        rating = 0
        length = len(composers)
        for compos in composers:
            movies = self.train.composer_movie(compos)
            if len(movies) == 0:
                length -= 1
                continue
            amount += len(movies)
            avgrating = 0
            for mov in movies:
                avgrating += self.train.movie_rating(mov)
            rating += avgrating / len(movies)
        if length == 0:
            return 0, self.errorvalue
        amount /= len(composers)
        rating /= len(composers)
        return amount, rating

    def get_budget(self, movie):
        """ returns budget of a movie """
        return self.val.movie_budget(movie)

#datainter = Datainteraction()
#print(datainter.director_values('Harry(2018)'))
