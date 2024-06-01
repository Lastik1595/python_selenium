import sqlite3
from english_bot.config import datebase_name


database_name = datebase_name


class EnglishBotDatabase:
    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def creating_users_db(database_name: str = database_name):
        """the function just creates sqllite datebase to save users information"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    user_id INTEGER,
                    first_name TEXT,
                    translation TEXT,
                    game TEXT,
                    question TEXT,
                    answer TEXT,
                    user_answer TEXT,
                    variants TEXT,
                    user_variants TEXT,
                    user_score INTEGER,
                    counter_user_score INTEGER

                    )
                """)

        connect.commit()
        connect.close()

    @staticmethod
    def creating_object_user_in_db(user_id: int, first_name: str, database_name: str = database_name):
        """Create a new object in db. the function gets user id from telegram and username"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('INSERT INTO Users (user_id, first_name,  translation, game, '
                       'question,answer, user_answer, variants, user_variants, '
                       'user_score, counter_user_score) '
                       'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)',
                       (user_id, first_name, "rus", "", "", "", "", "", "", 0, 0))
        connect.commit()
        connect.close()

    @staticmethod
    def looking_for_user_in_db(user_id: int, database_name: str = database_name) -> bool:
        """This function gets user id from telegram and returns True if the one in database
        and False if the one does not exist in database"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM Users WHERE user_id=?', (user_id,))
        user = cursor.fetchall()
        connect.close()
        if len(user) > 0:
            return True
        else:
            return False

    @staticmethod
    def checking_user_game(user_id: int, database_name: str = database_name) -> str | None:
        """the function cheks game which user is playing and returns the name of the game"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT game FROM Users WHERE user_id=?', (user_id,))
        game = cursor.fetchone()
        connect.close()
        try:
            return game[0]
        except TypeError:
            return None

    @staticmethod
    def updating_answer(user_id: int, answer: str, database_name: str = database_name):
        """the function updated  answer for the game"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET answer = ? WHERE user_id = ?', (answer, user_id))
        connect.commit()
        connect.close()

    @staticmethod
    def updating_question(question: str, user_id: int, database_name: str = database_name):
        """the function updated question for tge game"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET question = ? WHERE user_id = ?', (question, user_id))
        connect.commit()
        connect.close()

    @staticmethod
    def checking_question(user_id: int, database_name: str = database_name) -> str:
        """the function cheks question for user"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT question FROM Users WHERE user_id=?', (user_id,))
        queistion = cursor.fetchone()
        connect.close()
        try:
            return queistion[0]
        except TypeError:
            return ""

    @staticmethod
    def updating_user_game(user_id: int, database_name: str = database_name, game: str = None):
        """the function updayes user game"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET game = ? WHERE user_id = ?', (game, user_id))
        connect.commit()
        connect.close()

    @staticmethod
    def updating_user_translation(translation: str, user_id: int, database_name: str = database_name):
        """the function updates user translation
        rus means english to russian. turk means russian to english.
        do not blame me it is the api  I just use that"""

        if translation == "rus":
            translation = "turk"
        elif translation == "turk":
            translation = "rus"
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET translation = ? WHERE user_id = ?', (translation, user_id))
        connect.commit()
        connect.close()

    @staticmethod
    def checking_user_translation(user_id: int, database_name: str = database_name):
        """the function checks user translation"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT translation FROM Users WHERE user_id=?', (user_id,))
        translation = cursor.fetchone()
        connect.close()
        try:
            return translation[0]
        except TypeError:
            return None

    @staticmethod
    def checking_variants_for_user(user_id: int, database_name: str = database_name):
        """the function checks user variants"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT variants FROM Users WHERE user_id=?', (user_id,))
        variants = cursor.fetchone()
        connect.close()
        try:
            return variants[0].split()
        except TypeError:
            return None

    @staticmethod
    def updating_variants_for_user(user_id: int, variants: list, database_name: str = database_name):
        """the function updayes user game"""
        variants = " ".join(variants)
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET variants = ? WHERE user_id = ?', (variants, user_id))
        connect.commit()
        connect.close()

    @staticmethod
    def checking_answer(user_id: int, database_name: str = database_name) -> str:
        """the function cheks game which user is playing and returns the name of the game"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT answer FROM Users WHERE user_id=?', (user_id,))
        answer = cursor.fetchone()
        connect.close()
        try:
            return answer[0]
        except TypeError:
            return ""

    @staticmethod
    def updating_user_variants(user_id: int, var: list | None = None, database_name: str = database_name):
        """the function """
        var = " ".join(var)
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET user_variants = ? WHERE user_id = ?', (var, user_id))
        connect.commit()
        connect.close()

    @staticmethod
    def checking_user_score(user_id: int, database_name: str = database_name) -> int:
        """the function check user score"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT user_score FROM Users WHERE user_id=?', (user_id,))
        user_score = cursor.fetchone()
        connect.close()
        return int(user_score[0])

    @staticmethod
    def updating_score_count(user_id: int, win: int = 0, database_name: str = database_name):
        """the function updates counter of user wins if win +=1, else win =0"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET counter_user_score = ? WHERE user_id = ?', (win, user_id))
        connect.commit()
        connect.close()

    @staticmethod
    def checking_counter_user_score(user_id: int, database_name: str = database_name) -> int:
        """the function check user score"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT counter_user_score FROM Users WHERE user_id=?', (user_id,))
        counter_user_score = cursor.fetchone()
        connect.close()
        return int(counter_user_score[0])

    @staticmethod
    def updating_user_score(user_id: int, counter: int, database_name: str = database_name):
        """the function updates user_score in database"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET user_score = ? WHERE user_id = ?', (counter, user_id))
        connect.commit()
        connect.close()

    @staticmethod
    def checking_user_answer(user_id: int, database_name: str = database_name) -> str:
        """the function checks user answers and returns a str"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT user_answer FROM Users WHERE user_id=?', (user_id,))
        user_answer = cursor.fetchone()
        connect.close()
        if user_answer[0] is None:
            user_answer = ""
            return user_answer
        else:
            return user_answer[0]

    @staticmethod
    def updating_user_answer(user_id: int, user_answer: str | None = None, database_name: str = database_name):
        """the functions updates variant of user answer"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET user_answer = ? WHERE user_id = ?', (user_answer, user_id))
        connect.commit()
        connect.close()

    @staticmethod
    def checking_user_variants(user_id: int, database_name: str = database_name) -> list:
        """the function checks available variants for user and returns list of that """
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT user_variants FROM Users WHERE user_id=?', (user_id,))
        user_variants = cursor.fetchone()
        connect.close()
        if " " in user_variants[0]:
            user_variants = user_variants[0].split()
            return user_variants
        else:
            user_variants = list(user_variants)
            return user_variants

    @staticmethod
    def updating_user_rating(user_id: int, win: bool = True):
        """the fynction updates user rating"""
        if win is True:
            win = EnglishBotDatabase.checking_counter_user_score(user_id=user_id) + 1
            EnglishBotDatabase.updating_score_count(user_id=user_id, win=win)
        else:
            user_score = EnglishBotDatabase.checking_user_score(user_id=user_id)
            counter_user_score = EnglishBotDatabase.checking_counter_user_score(user_id=user_id)
            if counter_user_score > user_score:
                EnglishBotDatabase.updating_user_score(user_id=user_id, counter=counter_user_score)
            EnglishBotDatabase.updating_score_count(user_id=user_id)
