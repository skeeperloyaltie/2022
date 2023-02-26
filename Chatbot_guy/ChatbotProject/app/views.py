from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import levenshtein_distance
from chatterbot.trainers import ChatterBotCorpusTrainer


def index(request):
    template = loader.get_template('app.html')
    con = {}

    if request.method == 'POST':

        user_input = request.POST.get('input')
        chat = request.POST.get('content')
        print(user_input)

        # pass input to Chatbot, preprocessors=["chatterbot.preprocessors.clean_whitespace"],
        #https://github.com/gunthercox/ChatterBot/issues/1137
        #https://github.com/gunthercox/ChatterBot/issues/1216
        bot = ChatBot('Test',logic_adapters=[
        {
            #this block is working
             #'import_path': 'chatterbot.logic.BestMatch',
             #'default_response': 'I am sorry, I am so stupid I could be president of ...',
             ##'maximum_similarity_threshold': 0.60
            #'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
            ##'response_selection_method': 'chatterbot.response_selection.get_first_response'
            #'threshold': 0.10


            "import_path": "chatterbot.logic.BestMatch",
        },
            {
                'import_path': 'chatterbot.logic.BestMatch',
                #'threshold': 0.60,
                'maximum_similarity_threshold': 0.90,
                'default_response': "I am sorry, I didn't catched what you meant, but I am constantly learning. Could you please repeat your question in other words?"

            }
    ],)  # create the chatbot

        conv = open('app/chats.txt', 'r').readlines()
        trainer = ListTrainer(bot)
        trainer.train(conv)

        #29.04.2020: uncommented, since I only want to train once, due to performance; but you must uncomment this if you run it the first time
        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train('chatterbot.corpus.german')
        trainer.train('chatterbot.corpus.english')
        # FAQ in German Corpus 
  
        trainer.train('chatterbot.corpus.FAQ')

        if bot.get_response(user_input):
            resp = bot.get_response(user_input)
            print(resp)
            con = {'resp': resp, 'input': user_input}
        elif not bot.get_response(user_input):
            con = {}
    return HttpResponse(template.render(con, request))
