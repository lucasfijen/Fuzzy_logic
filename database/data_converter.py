import json
import pandas as pd
from random import shuffle

def load_tmdb_movies(path):
    """ Function that came with the database, found on Kaggle.com """
    df = pd.read_csv(path)
    df['release_date'] = pd.to_datetime(df['release_date']).apply(lambda x: x.date())
    json_columns = ['genres', 'keywords', 'production_countries', 'production_companies', 'spoken_languages']
    for column in json_columns:
        df[column] = df[column].apply(json.loads)
    return df

def load_tmdb_credits(path):
    """ Function that came with the database, found on Kaggle.com """
    df = pd.read_csv(path)
    json_columns = ['cast', 'crew']
    for column in json_columns:
        df[column] = df[column].apply(json.loads)
    return df

def split_train_val(credits, movie, ratio):
    """ This function splits the database into two sets, the training and
        validation set uses indices for this. So there is no information loss,
        each time this function is called a new random split is performed
        with the given ratio. """
    indexes = [i for i in range(len(credits))]
    shuffle(indexes)
    splitval = int(ratio * len(indexes))
    trainind = sorted(indexes[:splitval])
    valind = sorted([x for x in indexes if x not in trainind])
    return movie.iloc[trainind], credits.iloc[trainind], movie.iloc[valind], credits.iloc[valind]

def write_credits_csv(actfile, dirfile, comfile, specialfile, creditfile):
    """ Converts the credits database into the csv style that is beeing used
        in the rest of the code. """
    actfile = open(actfile, 'w')
    dirfile = open(dirfile, 'w')
    comfile = open(comfile, 'w')
    specialfile = open(specialfile, 'w')
    for i in creditfile.index.values:
        moviename = creditfile['title'][i].replace('#', '')
        cast = creditfile['cast'][i]
        for j in range(len(cast)):
            #write actors to file
            actfile.write(cast[j]['name'] + '%' + moviename + '\n')
        crew = creditfile['crew'][i]

        for j in range(len(crew)):
            # Write director to file
            if crew[j]['job'] == 'Director':
                dirfile.write(crew[j]['name'] + '%' + moviename + '\n')

            # Write composers to file
            if crew[j]['job'] == 'Original Music Composer':
                comfile.write(crew[j]['name'] + '%' + moviename + '\n')

            if crew[j]['department'] == 'Visual Effects':
                specialfile.write(crew[j]['name'] + '%' + moviename + '\n')
    actfile.close()
    dirfile.close()
    comfile.close()
    specialfile.close()

def write_movie_csv(busfile, ratfile, moviefile):
    """ Converts the movie database into the csv style that is beeing used
        in the rest of the code. """
    busfile = open(busfile, 'w')
    ratfile = open(ratfile, 'w')
    for i in moviefile.index.values:
        moviename = moviefile['title'][i].replace('#', '')
        busfile.write(moviename + '%' + str(moviefile['budget'][i]) + '\n')
        ratfile.write(moviename + '%' + str(moviefile['vote_average'][i]) + '\n')
    busfile.close()
    ratfile.close()

credits = load_tmdb_credits('tmdb_5000_credits.csv')
movie = load_tmdb_movies('tmdb_5000_movies.csv')

# Creates the training and validation set with a ratio of 0.8
trainmovie, traincredits, valmovie, valcredits = split_train_val(credits, movie, 0.8)
write_credits_csv('actors.csv', 'directors.csv', 'composers.csv', 'special-effects-companies.csv', traincredits)
write_movie_csv('business.csv', 'ratings.csv',  trainmovie)
write_credits_csv('valactors.csv', 'valdirectors.csv', 'valcomposers.csv', 'valspecial-effects-companies.csv', valcredits)
write_movie_csv('valbusiness.csv', 'valratings.csv', valmovie)
