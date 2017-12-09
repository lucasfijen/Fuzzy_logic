import numpy as np

directors = np.loadtxt('database/directors.csv', dtype='str', delimiter=',')
composers = np.loadtxt('database/composers.csv', dtype='str', delimiter=',')
actors = np.loadtxt('database/actors.csv', dtype='str', delimiter=',')
business = np.loadtxt('database/business.csv', dtype='str', delimiter=',')
special = np.loadtxt('database/special-effects-companies.csv', dtype='str', delimiter=',')
print(directors)
