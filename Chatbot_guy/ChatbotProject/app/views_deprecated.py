import json
import os
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer

class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)
    bot = ChatBot('Test')  # create the chatbot

    def post(self, request, bot, *args, **kwargs):

        conv = open('chats.txt', 'r').readlines()

        trainer = ListTrainer(bot)

        for _files in os.listdir('C:/Users/rehbergje/PycharmProjects/ChatbotProject/venv_py/files'):
            chats = open('C:/Users/rehbergje/PycharmProjects/ChatbotProject/files/' + _files, 'r').readlines()
            trainer.train(chats)

        request = input('You: ')
        return HttpResponse(request)



        # """
        # Return a response to the statement in the posted data.
        # * The JSON data should contain a 'text' attribute.
        # """
        # input_data = json.loads(request.body.decode('utf-8'))
        #
        # if 'text' not in input_data:
        #     return JsonResponse({
        #         'text': [
        #             'The attribute "text" is required.'
        #         ]
        #     }, status=400)
        #
        # response = self.chatterbot.get_response(input_data)
        #
        # response_data = response.serialize()
        #
        # return JsonResponse(response_data, status=200)

    def get(self, request, bot, *args, **kwargs):
        response = bot.get_response(request)

        return HttpResponse(response)
        # """
        # Return data corresponding to the current conversation.
        # """
        # return JsonResponse({
        #     'name': self.chatterbot.name
        # })