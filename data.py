import numpy as np

class Moviedata:
    """Creates a database object, with functions to get information"""
    def __init__(self, compo, direct, actor, busin, special, rat):
        self.composers = np.genfromtxt('database/' + compo + '.csv', dtype='str', delimiter=',')
        self.directors = np.genfromtxt('database/' + direct + '.csv', dtype='str', delimiter=',')
        self.actors = np.genfromtxt('database/' + actor + '.csv', dtype='str', delimiter=',')
        self.business = np.genfromtxt('database/' + busin + '.csv', dtype='str', delimiter=',')
        self.specials = np.genfromtxt('database/' + special + '.csv',
                                      dtype='str', delimiter=',')
        self.ratings = np.genfromtxt('database/' + rat + '.csv', dtype='str', delimiter=',')

    def composer_movie(self, composer):
        """Returns a numpy array with movies with music from composer"""
        return self.composers[self.composers[:, 0] == composer, 1]

    def director_movie(self, director):
        """Returns a numpy array with movies made by director"""
        return self.directors[self.directors[:, 0] == director, 1]

    def actor_movie(self, actor):
        """Returns a numpy array with movies in which actor stars"""
        return self.actors[self.actors[:, 0] == actor, 1]

    def special_movie(self, special):
        """ returns numpy array with movies created by special effect studio """
        return self.specials[self.specials[:, 0] == special, 1]

    def movie_composer(self, movie):
        """ returns numpy array with composers for a movie, usually this is one"""
        return self.composers[self.composers[:, 1] == movie, 0]

    def movie_director(self, movie):
        """ returns numpy array with directors of a movie """
        return self.directors[self.directors[:, 1] == movie, 0]

    def movie_actor(self, movie):
        """ returns numpy array with actors playing in a movie """
        return self.actors[self.actors[:, 1] == movie, 0]

    def movie_special(self, movie):
        """returns numpy array with special effect studios per movie """
        return self.specials[self.specials[:, 1] == movie, 0]

    def movie_budget(self, movie):
        """returns budget for a movie, just to be sure, it can handle multiple
           known budgets as well, and will return the max budget in that case
           if no budget is given, it will return a minus
           """
        budgets = self.business[self.business[:, 0] == movie, 1]
        if len(budgets) == 0:
            return -1
        return max(budgets.astype(int))

    def movie_rating(self, movie):
        """returns rating of a movie, just to be sure, it can handle multiple
           known ratings as well, and will return the max rating in that case
           """
        ratings = self.ratings[self.ratings[:, 0] == movie, 1]
        if len(ratings) == 0:
            return 0
        return max(ratings.astype(float))
