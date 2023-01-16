import pandas as pd
import random as rnd
rand = rnd.Random()
z = rand.randint(1,10)

uebungen = pd.read_csv('/Users/Andrin/Documents/Python_code/Trainings-Generator/uebungen.csv')

print(uebungen['legs'][9])
