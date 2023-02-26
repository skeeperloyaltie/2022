import nltk
import random
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import csv 
import json
import pickle
import pandas as pd

training_dataset = pd.read_csv('dataset/Training.csv')
test_dataset = pd.read_csv('dataset/Testing.csv')

# use nltk to tokenize the sentences for a medical chatbot on symptoms and diagnosis

# tokenize the training data
training_data = []
for i in range(0, len(training_dataset)):
    # get the sentence
    sentence = training_dataset['Sentence'][i]
    # get the label
    label = training_dataset['Label'][i]
    # append the training data
    training_data.append([sentence, label])
    
# tokenize the test data
test_data = []
for i in range(0, len(test_dataset)):
    # get the sentence
    sentence = test_dataset['Sentence'][i]
    # get the label
    label = test_dataset['Label'][i]
    # append the training data
    test_data.append([sentence, label])
    
# create a data structure to hold the words and tags
words = []
tags = []

# add unique words and tags to the data structure
for sentence in training_data:
    # tokenize the sentence
    for word in nltk.word_tokenize(sentence[0]):
        words.append(word)
    # append the tag
    tags.append(sentence[1])
    
# create a dictionary that maps each word to a unique index
word_index = {}
for i, word in enumerate(nltk.word_tokenize(str(words))):
    word_index[word] = i + 1

# create a list of all tags
tags = [tag for sentence in training_data for tag in sentence[1].split()]
tag_index = {}
for i, tag in enumerate(tags):
    tag_index[tag] = i + 1

# create the training data
X = []
y = []
for sentence in training_data:
    # tokenize the sentence
    for word in nltk.word_tokenize(sentence[0]):
        # add the word index to X
        X.append(word_index[word])
    # add the tag index to y
    for tag in sentence[1].split():
        y.append(tag_index[tag])
        
# create the test data
X_test = []
y_test = []
for sentence in test_data:
    # tokenize the sentence
    for word in nltk.word_tokenize(sentence[0]):
        # add the word index to X
        X_test.append(word_index[word])
    # add the tag index to y
    for tag in sentence[1].split():
        y_test.append(tag_index[tag])
        
# create the neural network
net = tflearn.input_data(shape=[None, len(X[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(y[0]), activation='softmax')
net = tflearn.regression(net)

# train the neural network
model = tflearn.DNN(net)
model.fit(X, y, n_epoch=1000, batch_size=8, show_metric=True)

# save the model
model.save('model/model.tflearn')

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return numpy.array(bag)

# create the chatbot interative interface
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = list(tags)[results_index]
        data = {"input": inp, "tag": tag}
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        print(random.choice(responses))
        
while True:
    chat()

