#************************************************************
# Author:           Grayson Hanna
# Lab:              6
# Description:      Main driver for the video game collection.
#                   Retrieves game information and displays
#                   each game's properties to the console.
# Input:            None
# Output:           Welcome message and video game records.
#************************************************************


from Game import Game


def intro_message():

    # Explain the program before displaying the game records.
    print("--------------------------------------------------------------")
    print("Video Game Collection")
    print("--------------------------------------------------------------\n")

    print("This program displays information about popular video games.")
    print("The information includes the game title, release year,")
    print("platform, and estimated copies sold.\n")


def display_games(game_list):

    # Display a heading before listing the games.
    print("--------------------------------------------------------------")
    print("Game Collection")
    print("--------------------------------------------------------------")

    # Loop through each Game object and display its properties.
    for game in game_list:

        print(game.get_title(), game.get_year(),
              game.get_platform(), str(game.get_sales()) + " million")

    print("--------------------------------------------------------------")


def main():

    intro_message()

    # Retrieve the list of Game objects.
    game_list = Game.read_games()

    # Display the information for each game.
    display_games(game_list)


# Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()