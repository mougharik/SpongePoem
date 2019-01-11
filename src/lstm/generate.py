#!/usr/bin/env python3

'''
Text-Generation File

'''

import sys
import random
import numpy as np
import tensorflow.keras as keras
from tensorflow.keras import layers

import config as c
from model import Model
from vectorize import TextVec

def main():
    tensorData = TextVec(c.dataDir, c.batchSize, c.seqLen, c.step)
    SpongeRNN = Model(c.rnnSize, c.loss, c.activation, c.seqLen, tensorData.vocabSize)
    generateText(c, SpongeRNN, tensorData)


def generateText(c, SpongeRNN, tensorData):
    '''
    This portion is modeled from Chapter 8 (Text Generation with LSTM) in the book:
        "Deep Learning with Python" - Francois Challet
    '''
    for i in range(1, c.epochs+1):
        print('\n\nEpoch: ', i, file=open('../../data/results.txt', 'a'))
        sys.stdout.write(str(i) + '\n')
        SpongeRNN.model.fit(tensorData.x, tensorData.y, batch_size=c.batchSize, epochs=1)
        startIndex = random.randint(0, tensorData.senLen - tensorData.seqLen - 1)
        generatedText = tensorData.data[startIndex:startIndex + tensorData.seqLen]
        print('Generating with seed: "' + generatedText + '"', file=open('../../data/results.txt', 'a'))

        for temp in [0.5, 0.7, 1.0, 1.2]:
            print('\n\nTemperature: ', temp, file=open('../../data/results.txt', 'a'), end="\n\n")
            print(generatedText, file=open('../../data/results.txt', 'a'), end="")

            for i in range(400):
                sampled = np.zeros((1, tensorData.seqLen, tensorData.vocabSize))
                for j, char in enumerate(generatedText):
                    sampled[0, j, tensorData.charMap[char]] = 1

                preds = SpongeRNN.model.predict(sampled, verbose=0)[0]
                nextIndex = SpongeRNN.sample(preds, temp)
                nextChar = tensorData.vocab[nextIndex]
                generatedText += nextChar
                generatedText = generatedText[1:]
                print(nextChar, file=open('../../data/results.txt', 'a'), end="")

    keras.models.save_model(SpongeRNN.model,
                            '../../data/SpongeRNN',
                            overwrite=True,
                            include_optimizer=True
    )


if __name__ == '__main__':
    main()
