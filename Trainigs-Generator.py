import pandas as pd
import random as rnd
from datetime import date

def dataprep():
    uebungen = pd.read_csv('/Users/Andrin/Documents/Python_code/Trainings-Generator/uebungen.csv')
    counter = uebungen.count(axis=0)
    DL = uebungen[uebungen['legs2'].notnull()].index.tolist()
    DC = uebungen[uebungen['core2'].notnull()].index.tolist()
    return uebungen, counter,DL, DC

def setup(counter):
    print('Training generierern für:')
    training = []
    kinds = ['warmup', 'Bein', 'core', 'Ergo']
    prompt = 'Wie viele {}-übungen?:'
    for x in range(4):
        training.append(int(input(prompt.format(kinds[x]))))
        while training[x] > counter[x]:
            print("Limit ist", counter[x])
            training[x] = int(input(prompt.format(kinds[x])))
    return training

def generator(num,uebungen,DL, DC,rev,maxi):
    flag = False
    i = 0
    table = []
    rng = range(num)
    rand = rnd.sample(rng, num)
    while i < len(rand):
        table,loopback,flag = doubleExecs(flag,uebungen,table,i,rand,rev)
        if rand[i] in DL and rev == 1 and loopback == False:
            flag = True
            print(table)
        if rand[i] in DC and rev == 2 and loopback == False:
            flag = True
            print(table)
        i +=1
    while num < maxi:
        table.append('')
        num += 1
    return table

def doubleExecs(flag,uebungen,table,i,rand,rev):
    loopback = False
    if flag == True:
        step = i-1
        table.append(uebungen[uebungen.columns[rev+4]][rand[step]]) 
        flag = False
        loopback = True
    else: table.append(uebungen[uebungen.columns[rev]][rand[i]])
    return table, loopback, flag

def main():
    df = pd.DataFrame()
    data,counter,DL, DC = dataprep() # data = df, counter = warmup 15 (df), doubles = [0,1,3,4]
    training = setup(counter) # Trainging = [1,1,1,1]
    maxi = max(training)
    for i,x in enumerate(training):
        if x != 0:
            df[data.columns[i]] = generator(x,data,DL,DC,i,maxi)
    df.to_csv('/Users/Andrin/Desktop/training{}.csv'.format(date.today()))

if __name__ == '__main__':
    main()