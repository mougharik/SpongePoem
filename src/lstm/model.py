#!/usr/bin/env python3
'''
LSTM RNN Model Class

'''

import sys
import random
import numpy as np
import tensorflow.keras as keras
from tensorflow.keras import layers


class Model(object):
    '''
    This portion is modeled from Chapter 8 (Text Generation with LSTM) in the book:
        "Deep Learning with Python" - Francois Challet
    '''
    def __init__(self, rnnSize, rnnLoss, rnnActivation, seqLen, vocabSize):
        '''
        Model Creation
            - using keras sequential model
            - adds a LSTM layer wtih rnnSize (default is 128), and input shape that is determined
                by seqLen (default 40) and vocabSize (default from data is 27)
            - adds a Dense layer with input size of vocabSize and uses 'softmax' activation
            - optimizer uses RMSprop (root mean square propogation)
            - compiles model using 'categorical crossentropy' loss function
        '''
        self.model = keras.models.Sequential()
        self.model.add(layers.LSTM(rnnSize, input_shape=(seqLen, vocabSize)))
        self.model.add(layers.Dense(vocabSize, activation=rnnActivation))
        self.optimizer = keras.optimizers.RMSprop(lr=0.01)
        self.model.compile(loss=rnnLoss, optimizer=self.optimizer)

    def sample(self, pred, temperature=1.0):
        '''
        Sample Function
            - takes in probabily distribution from the model, reweights the distribution and
                selects the next character index to use
        '''
        pred = np.asarray(pred).astype('float64')
        pred = np.log(pred) / temperature
        expPred = np.exp(pred)
        pred = expPred / np.sum(expPred)
        prob = np.random.multinomial(1, pred, 1)
        return np.argmax(prob)
