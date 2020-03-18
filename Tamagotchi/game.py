from tamagotchi import Tamagotchi, Egg
import random
import time
import datetime


class Game:

    @staticmethod
    def main_menu():
        """
        The game will take place in here. There will be choices that the user can select from
        and non-choices will not be accepted.
        """
        game_run = True
        print("Welcome to the game of Tamagotchi!\n")
        while game_run:
            yes = "y"
            no = "n"
            choice = input("There is no Tamagotchi alive right now. Would you like to hatch one? Y or N\n")
            if choice.upper() == yes.upper():
                pokemon = Egg().hatch()  # hatches the pokemon here

                print(f"{pokemon.get_name()} was hatched!")
                pokemon_life = True

                while pokemon_life:  # Keep iterating until the tamagotchi dies
                    if pokemon._health <= 0:
                        print(f"{pokemon.get_name()} has died! Resetting game!\n")
                        return main()

                    current_time = Game.create_timer()
                    pokemon_choice = (input("1. Check status of pokemon\n"
                                            "2. Feed Pokemon\n"
                                            "3. Play with Pokemon\n"
                                            "4. Exit\n"))
                    if pokemon_choice == "1":
                        pokemon.status_messages(current_time)

                    elif pokemon_choice == "2":
                        pokemon_feed_choice = (input("1. Feed Pokemon Food\n"
                                                     "2. Feed Pokemon Medicine\n"))
                        if pokemon_feed_choice == "1":
                            pokemon.feed_menu()  # goes into the feed_menu() that calls feed()
                        elif pokemon_feed_choice == "2":
                            pokemon.feed_medicine()
                        else:
                            print("Not a valid command...")

                    elif pokemon_choice == "3":
                        pokemon.play()
                    elif pokemon_choice == "4":
                        print("Exiting game... Goodbye!")
                        game_run = False
                        break
                    else:
                        print("Not a valid command...")

            elif choice.upper() == no.upper():
                print("Okay, have a good day!\n")
                game_run = False
                break
            else:
                print("Not a valid choice!\n")

    @staticmethod
    def create_timer():
        """
        Purpose is to keep track of the previous time so that it can figure out how much
        time has passed
        """
        now = time.time()
        return now


def main():
    game = Game()
    game.main_menu()


if __name__ == '__main__':
    main()
