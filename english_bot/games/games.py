import requests
import random
from english_bot.api.headers import GuessingGameHeaders
from english_bot.api.urls import GuessingGameUrls
from english_bot.config import datebase_name
database_name=datebase_name
from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase
class Games():
    def __init__(self, user_id, user_param):
        self.user_id = user_id
        self.user_param = user_param





    def gusesing_game(self,user_id,user_param):
        database = EnglishBotDatabase(user_id)
        database.updating_user_game(user_id=user_id, game=user_param)
        translation = database.checking_user_translation(user_id=user_id)
        question, answer, variants = Games.getting_data_guessing_game(translation=translation, user_param=user_param)
        database.updating_answer( answer=answer,user_id=user_id)
        database.updating_variants_for_user(user_id=user_id, variants=variants)
        database.updating_question(user_id=user_id, question=question)
        return question, variants

    def getting_data_guessing_game(self,user_param: str, headers: str=GuessingGameHeaders.headers, params :str = GuessingGameHeaders.params_game, translation : str = "rus") -> tuple:
        """getting the guessind word game data"""
        params["slovar"]=user_param
        params["first"]=translation
        question = ""
        answer = ""
        variants = []
        response = requests.get(GuessingGameUrls.url, headers = headers, params=params).json()
        question = response["question"]
        answer = response["answer"]
        variants = list(response["variants"])
        return question, answer, variants

    def getting_constcuctor_games(self,translation: str="rus", user_param: str="v",  params :str = GuessingGameHeaders.params_game,
                                  headers: str=GuessingGameHeaders.headers):
        params["slovar"] = user_param
        params["first"] = translation
        question = ""
        answer = ""
        response = requests.get(GuessingGameUrls.url, headers=headers, params=params).json()
        question = response["question"]
        answer = response["answer"]
        print(answer)
        variants=Games.random_constructor_variants(answer)
        return question, answer, variants

    def random_constructor_variants(self, answer: str) -> list:
        """the function gets strings and splits them into lists
        and return the lists with random words of letters of the string"""

        if " " in answer:
            answer = answer.split()
        else:
            answer = list(answer)
        variants=[]
        while len(variants) != len(answer):
            item=answer[random.randrange(0,len(answer))]
            if item not in variants:
                variants.append(item)
        return variants


