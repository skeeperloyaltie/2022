from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
import pymysql
from django.http import HttpResponse
import numpy
import tflearn
import tensorflow
import random
import json
import pickle
import nltk
import pandas as pd
from nltk.stem.lancaster import LancasterStemmer

training_data = pd.readcsv('dataset/Training.csv')
test_data = pd.readcsv('dataset/Testing.csv')
options = 'none'

tensorflow.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training_data[0][0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(training_data[0][1].split()), activation='softmax')
net = tflearn.regression(net)
model = tflearn.DNN(net)
# model.load('model/model.tflearn')
def chat(request):
    global options
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['message'])
        print(request.POST['message'].lower())
        print(request.POST['message'].lower().split())
        print(request.POST['message'].lower().split()[-1])
        print(request.POST['message'].lower().split()[-1].split('.')[0])
        print(request.POST['message'].lower().split()[-1].split('.')[0].split('?')[0])
        print(request.POST['message'].lower().split()[-1].split('.')[0].split('?')[0].split('!')[0])
        print(request.POST['message'].lower().split()[-1].split('.')[0].split('?')[0].split('!')[0].split('-')[0])
        print(request.POST['message'].lower().split()[-1].split('.')[0].split('?')[0].split('!')[0].split('-')[0].split(' ')[-1])
        print(request.POST['message'].lower().split()[-1].split('.')[0].split('?')[0].split('!')[0].split('-')[0].split(' ')[-1])
        
    
    else:
        return render(request, 'chats/index.html')
    return render(request, 'chats/index.html')



def chats__(request):
    return render(request, 'chats/index.html')
