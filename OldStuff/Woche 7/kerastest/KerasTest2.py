# LSTM for sequence classification in the IMDB dataset
import numpy
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.layers import Dropout
from keras import optimizers
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
import json
from random import shuffle


def normalizeData(X, y):
    largestX = -1
    largestY = -1
    for x_ in X:
        for _x_ in x_:
            if largestX < _x_:
                largestX = _x_

    for y_ in y:
        if largestY < y_:
            largestY = y_

    for x_ in X:
        for _x_ in x_:
            _x_ = float(_x_) / float(largestX * len(y))

    for y_ in y:
        y_ = float(y_) / float(largestY * len(y) )
    return X, y

Train = json.load(open('EncodedSetSmall.json'))['data']
Test = json.load(open('EncodedSetSmall.json'))['data']

# fix random seed for reproducibility
numpy.random.seed(7)

_X_train_ = [t[0] for t in Train]
y_train = [t[1] for t in Train]

X_test = [t[0] for t in Test]
y_test = [t[1] for t in Test]


# truncate and pad input sequences
sequence_length = -1
top_words = -1
avgsequence_length = 0
for x in _X_train_:
    avgsequence_length += len(x)
    if sequence_length < len(x):
        sequence_length = len(x)
for x in X_test:
    if sequence_length < len(x):
        sequence_length = len(x)
for x in _X_train_:
    for i in x:
        if i > top_words:
            top_words = i

avgsequence_length = int(avgsequence_length / len(_X_train_))
sequence_length = 32
X_train = sequence.pad_sequences(_X_train_, maxlen=sequence_length)
X_test = sequence.pad_sequences(X_test, maxlen=sequence_length)
top_words += 1

X_train, y_train = normalizeData(X_train, y_train)
# create the model
model = Sequential()

model.add(Embedding(top_words, output_dim =sequence_length , input_length=sequence_length))

model.add(LSTM(avgsequence_length*3, return_sequences=True))
model.add(LSTM(avgsequence_length*4, return_sequences=True))
model.add(LSTM(avgsequence_length*5, return_sequences=True))
model.add(LSTM(avgsequence_length*6, return_sequences=True))
model.add(LSTM(avgsequence_length*12, return_sequences=True))
model.add(LSTM(avgsequence_length*6, return_sequences=True))
model.add(LSTM(avgsequence_length*5, return_sequences=True))
model.add(LSTM(avgsequence_length*4, return_sequences=True))
model.add(LSTM(avgsequence_length*3, return_sequences=True))
model.add(LSTM(avgsequence_length*2, return_sequences=True))
model.add(LSTM(avgsequence_length))
model.add(Dense(len(y_test)))
model.add(Dense(1))


rms = optimizers.RMSprop(lr=1e-5)
model.compile(loss='mean_absolute_percentage_error', optimizer=rms, metrics=['accuracy'])
print(model.summary())
for i in range(10):
    for x in _X_train_:
        shuffle(x)
    X_train = sequence.pad_sequences(_X_train_, maxlen=sequence_length)
    model.fit(X_train, y_train, epochs=10)

# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))


