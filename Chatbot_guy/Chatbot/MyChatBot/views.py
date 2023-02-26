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
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

with open("model/smoking.pickle", "rb") as f:
    swords, slabels, straining, soutput = pickle.load(f)
f.close()

with open("model/drugs.pickle", "rb") as f:
    dwords, dlabels, dtraining, doutput = pickle.load(f)
f.close()

with open("model/alcohol.pickle", "rb") as f:
    awords, alabels, atraining, aoutput = pickle.load(f)
f.close()

option = 'none'
tensorflow.reset_default_graph()
net = tflearn.input_data(shape=[None, len(straining[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(soutput[0]), activation="softmax")
net = tflearn.regression(net)
smoking_model = tflearn.DNN(net)
#smoking_model.load("model/smokingmodel.tflearn")
smoking_model.fit(straining, soutput, n_epoch=1000, batch_size=8, show_metric=True)

tensorflow.reset_default_graph()
dnet = tflearn.input_data(shape=[None, len(dtraining[0])])
dnet = tflearn.fully_connected(dnet, 8)
dnet = tflearn.fully_connected(dnet, 8)
dnet = tflearn.fully_connected(dnet, len(doutput[0]), activation="softmax")
dnet = tflearn.regression(dnet)
drugs_model = tflearn.DNN(dnet)
#drugs_model.load("model/drugsmodel.tflearn")
drugs_model.fit(dtraining, doutput, n_epoch=1000, batch_size=8, show_metric=True)

tensorflow.reset_default_graph()
anet = tflearn.input_data(shape=[None, len(atraining[0])])
anet = tflearn.fully_connected(anet, 8)
anet = tflearn.fully_connected(anet, 8)
anet = tflearn.fully_connected(anet, len(aoutput[0]), activation="softmax")
anet = tflearn.regression(anet)
alcohol_model = tflearn.DNN(anet)
#alcohol_model.load("model/alcoholmodel.tflearn")
alcohol_model.fit(atraining, aoutput, n_epoch=1000, batch_size=8, show_metric=True)

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

def Option(request):
    if request.method == 'GET':
       return render(request, 'Option.html', {})
    
def MyChatBot(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def User(request):
    if request.method == 'GET':
       return render(request, 'User.html', {})

def Logout(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def test(request):
    if request.method == 'GET':
       return render(request, 'test.html', {})

def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})

def BotOption(request):
    if request.method == 'POST':
      global option
      option = request.POST.get('t1', False)
      context= {'data':'You selected '+option+" Bot"}
      return render(request, 'UserScreen.html', context)

def getOutput(bog,model,labels,data):
    results = model.predict(bog)
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    str = "no result found"
    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
            str = random.choice(responses)
    return str        
    

def ChatData(request):
    if request.method == 'GET':
        question = request.GET.get('mytext', False)
        if option == 'Smoking':
            words = []
            data = []
            with open("model/smoking.pickle", "rb") as f:
                words, labels, training, output = pickle.load(f)
            f.close()
            with open("dataset/smoking.json") as file:
                data = json.load(file)
            file.close()
            str = getOutput([bag_of_words(question, words)],smoking_model,labels,data)
            print(question+" "+str)
            return HttpResponse(str, content_type="text/plain")
        if option == 'Drugs':
            words = []
            data = []
            with open("model/drugs.pickle", "rb") as f:
                words, labels, training, output = pickle.load(f)
            f.close()
            with open("dataset/drugs.json") as file:
                data = json.load(file)
            file.close()
            str = getOutput([bag_of_words(question, words)],drugs_model,labels,data)
            print(question+" "+str)
            return HttpResponse(str, content_type="text/plain")
        if option == 'Alcohol':
            words = []
            data = []
            with open("model/alcohol.pickle", "rb") as f:
                words, labels, training, output = pickle.load(f)
            f.close()
            with open("dataset/alcohol.json") as file:
                data = json.load(file)
            file.close()
            str = getOutput([bag_of_words(question, words)],alcohol_model,labels,data)
            print(question+" "+str)
            return HttpResponse(str, content_type="text/plain")


def UserLogin(request):
    if request.method == 'POST':
      username = request.POST.get('username', False)
      password = request.POST.get('password', False)
      index = 0
      con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'chatbot',charset='utf8')
      with con:    
          cur = con.cursor()
          cur.execute("select * FROM register")
          rows = cur.fetchall()
          for row in rows: 
             if row[0] == username and password == row[1]:
                index = 1
                break		
      if index == 1:
       context= {'data':'welcome '+username}
       return render(request, 'Option.html', context)
      else:
       context= {'data':'login failed'}
       return render(request, 'User.html', context)

def Signup(request):
    if request.method == 'POST':
      username = request.POST.get('username', False)
      password = request.POST.get('password', False)
      contact = request.POST.get('contact', False)
      email = request.POST.get('email', False)
      address = request.POST.get('address', False)
      db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'chatbot',charset='utf8')
      db_cursor = db_connection.cursor()
      student_sql_query = "INSERT INTO register(username,password,contact,email,address) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
      db_cursor.execute(student_sql_query)
      db_connection.commit()
      print(db_cursor.rowcount, "Record Inserted")
      if db_cursor.rowcount == 1:
       context= {'data':'Signup Process Completed'}
       return render(request, 'Register.html', context)
      else:
       context= {'data':'Error in signup process'}
       return render(request, 'Register.html', context)
