#!/usr/bin/env python3

'''
Vectorize text input data and create vocab file

'''

import os
import re
import numpy as np

class TextVec(object):
    '''
    TextVec Class
        - Builds character map from unique alphabetical and whitespace characters in data
        - Vectorizes an x and y with shapes determined by sentence length, max sequence length,
            and size of vocab (unique characters)
    '''
    def __init__(self, dataDir, batchSize, seqLen, step):
        self.inputData = os.path.join(dataDir, 'spongeTranscript.txt')
        self.seqLen = seqLen
        self.step = step

        print('Vectorizing input data to build vocabulary map and respective tensors.')
        self.preprocess(self.inputData)

    def preprocess(self, inputData):
        '''
        Preprocess Function
            - reads input data and removes any non-whitespace/non-alphabetical characters
            - packs sequences of seqLen size into 'sentences' list, and its respective targets
                in the targets list
            - calculates length of sentences, size and a list of the vocab, and a character map
                that maps unique characters to their index in the vocab list
            - one-hot encodes the characters into binary
        '''
        with open(inputData, 'r') as x:
            data = x.read().lower()
        regex = re.compile('[^a-zA-z\s]|[\[\]]')
        data = regex.sub('', data)
        data = data.replace(u'\xa0', u' ')
        data = data.replace(u'\n', u' ')

        '''
        This portion is modeled from Chapter 8 (Text Generation with LSTM) in the book:
            "Deep Learning with Python" - Francois Challet
        '''
        sentences = []
        targets = []
        for x in range(0, len(data) - self.seqLen, self.step):
            sentences.append(data[x:x + self.seqLen])
            targets.append(data[x + self.seqLen])

        self.data = data
        self.senLen = len(sentences)
        self.vocab = sorted(list(set(data)))
        self.vocabSize = len(self.vocab)
        self.charMap= dict((i, self.vocab.index(i)) for i in self.vocab)

        self.x = np.zeros((self.senLen, self.seqLen, self.vocabSize), dtype=np.bool)
        self.y = np.zeros((self.senLen, self.vocabSize), dtype=np.bool)
        for i, sen in enumerate(sentences):
            for j, char in enumerate(sen):
                self.x[i, j, self.charMap[char]] = 1
            self.y[i, self.charMap[targets[i]]] = 1


