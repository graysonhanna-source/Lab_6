#************************************************************
# Author:           Grayson Hanna
# Lab:              6
# Description:      Contains the Game class, which stores
#                   video game information and provides
#                   methods to access and change its values.
#************************************************************

from Database import Database


class Game:

    def __init__(self, title, year, platform, sales):

        # Store game information as private properties.
        self.__title = title
        self.__year = year
        self.__platform = platform
        self.__sales = sales

    # Setters for changing game properties.
    def set_title(self, title):
        self.__title = title

    def set_year(self, year):
        self.__year = year

    def set_platform(self, platform):
        self.__platform = platform

    def set_sales(self, sales):
        self.__sales = sales

    # Getters for accessing game properties.
    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_platform(self):
        return self.__platform

    def get_sales(self):
        return self.__sales

    @staticmethod
    def read_games():

        # Retrieve game dictionaries from the database class.
        game_data = Database.read_games()
        game_list = []

        # Convert each dictionary into a Game object.
        for data in game_data:
            game = Game(data["title"], data["year"],
                        data["platform"], data["sales"])

            game_list.append(game)

        return game_list