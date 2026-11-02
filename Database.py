#************************************************************
# Author:           Grayson Hanna
# Lab:              6
# Description:      Provides sample video game data for the
#                   Game class.
#************************************************************


class Database:

    @classmethod
    def read_games(cls):

        # Store video game information in a list of dictionaries.
        game_data = [
            {"title": "Minecraft", "year": 2011,
             "platform": "PC", "sales": 300},

            {"title": "Grand Theft Auto V", "year": 2013,
             "platform": "Multiple", "sales": 200},

            {"title": "Tetris", "year": 1984,
             "platform": "Multiple", "sales": 100},

            {"title": "Wii Sports", "year": 2006,
             "platform": "Wii", "sales": 83},

            {"title": "Mario Kart 8", "year": 2014,
             "platform": "Nintendo Switch", "sales": 78}
        ]

        return game_data