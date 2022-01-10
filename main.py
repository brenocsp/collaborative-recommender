import sys
import time

import pandas as pd
import numpy as np

from src.LatentFactorModelRecommender import LatentFactorModelRecommender

def main():
    startTime = time.time()

    with open(sys.argv[1], 'r') as f:
        ratings = pd.read_csv(f, sep='[:|,]', engine='python')
        
    with open(sys.argv[2], 'r') as f:
        targets = pd.read_csv(f, sep='[:|,]', engine='python')

    training = ratings.sample(frac=0.8, random_state=8)
    validation = ratings.drop(training.index.tolist())

    recommender = LatentFactorModelRecommender(learningRate=0.01, regularizationFactor=0.05, nEpochs=50, nFactors=25, stopThreshold=0.000001)

    # Caso seja necessário apenas printar na tela os valores ou gerar um arquivo, modifique os parametros saveToFile e printOnConsole
    recommender.runRecommender(training, validation, targets, startTime, saveToFile=False, printOnConsole=True)

    print("Time: %s seconds " % (time.time() - startTime))


main()
