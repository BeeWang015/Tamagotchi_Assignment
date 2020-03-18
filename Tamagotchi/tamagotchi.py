import random
import time
import datetime
import abc


class Tamagotchi(abc.ABC):
    """
    An abstract class Tamagotchi that initializes some values that will be used amongst all different
    Tamagotchi's health, happiness, and hunger decay rates. It will also store potential food and
    activities that the Pokemon can use.
    """

    def __init__(self, name, health, happiness, hunger):
        self._name = name
        self._health = health
        self._happiness = happiness
        self._hunger = hunger

        self.health_decay = 0
        self.hunger_decay = 0
        self.happiness_decay = 0

        self.isSick = False

        self.food = ["Blueberry", "Strawberry", "Coca-Cola", "Mocha"]
        self.activities = ["Tag", "Jump Rope", "Hide and Seek", "Fetch"]

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_health(self, health):
        self._health = health

    def get_health(self):
        return f"{'%.2f' % self._health}"

    def set_happiness(self, happiness):
        self._happiness = happiness

    def get_happiness(self):
        return f"{'%.2f' % self._happiness}"

    def set_hunger(self, hunger):
        self._hunger = hunger

    def get_hunger(self):
        return f"{'%.2f' % self._hunger}"

    def status_messages(self, timer):
        """
        Checks the status of the Tamagotchi but also determines how much time has passed
        :param timer: This will be the previous time
        """
        self.speak()

        elapsed_time = time.time() - timer
        self.hunger_decay_rate(elapsed_time)
        self.happiness_decay_rate(elapsed_time)

        if self._health < 50:
            self.get_sick()
        self.health_decay_rate(elapsed_time)

        print(f"{self.get_name()} is at Health: {self.get_health()}, Happiness, {self.get_happiness()},"
              f" Hunger: {self.get_hunger()}\n")

    def hunger_decay_rate(self, timer):
        time_loop = 0
        while time_loop < timer:
            if self._hunger >= 100:
                self._hunger = 100
                time_loop += 1
            else:
                self._hunger += self.hunger_decay
                time_loop += 1
        return self._hunger

    def happiness_decay_rate(self, timer):
        time_loop = 0

        while time_loop < timer:
            self._happiness -= self.happiness_decay
            time_loop += 1
        return self._happiness

    def health_decay_rate(self, timer):
        time_loop = 0

        while time_loop < timer:
            if self._hunger == 100:
                self._health -= self.health_decay * 2

                if self._health <= 0:
                    self._health = 0
                    return

                time_loop += 1
            else:
                self._health -= self.health_decay

                if self._health == 0:
                    self._health = 0
                    return

                time_loop += 1
        return self._health

    def feed_menu(self):
        """
        Sets up choices for the user to choose from
        """
        print("\nSelect the food you would like")
        food_choice = (input("1. Blueberry\n"
                             "2. Strawberry\n"
                             "3. Coca-cola\n"
                             "4. Mocha\n"))
        choice = ["1", "2", "3", "4"]  # makes sure to check for valid inputs
        if food_choice in choice:
            food_choice = int(food_choice)
            self.feed(food_choice)
        else:
            print("Not a valid input...")

    def feed(self, food_picked):
        """
        Chooses food from random and feeds it to the tamagotchi. There is a chance
        that the tamagotchi will receive its favourite food. If it does, there is a
        10% bonus for hunger.
        """
        chosen_food = self.food[food_picked - 1]
        if chosen_food == self._favourite_food:
            self._hunger -= 20 * 1.10

            if self._hunger <= 0:
                print(f"{self.get_name()} is full")
                print(f"{self.get_name()} was fed its favourite food: {self._favourite_food}\n")
                self._hunger = 0
                return

            print(f"{self.get_name()} was fed its favourite food: {self._favourite_food}\n")
            return
        else:
            self._hunger -= 20

            if self._hunger <= 0:
                print(f"{self.get_name()} is full")
                print(f"{self.get_name()} was fed: {chosen_food}\n")
                self._hunger = 0
                return

            print(f"{self.get_name()} was fed: {chosen_food}\n")
            return

    def feed_medicine(self):
        """
        Medicine gives back 40 health and will cap out health at 100
        """
        self._health += 40
        if self._health >= 50:

            if self._health > 100:
                self._health = 100
                print(f"{self._name} is healthy!\n")
                return

            self.isSick = False
            print(f"{self._name} is healthy!\n")
            return

        else:
            print(f"{self._name} feels a little better.\n")
            return

    def get_sick(self):
        """
        Will print out a sick statement if the health is below 50
        """

        self.isSick = True
        print(f"{self._name} is sick! Feed it some medicine!")

    def play(self):

        """
        Play with a pokemon and keep the happiness capped at 100 otherwise adds
        10 per play action.
        """
        activity_choice = random.choice(self.activities)

        if self._happiness >= 100:
            self._happiness = 100
            print(f"{self._name} just played {activity_choice} with you!")
            print(f"{self._name} is having a blast!\n")
            return

        else:
            self._happiness += 15

            if self._happiness >= 100:
                self._happiness = 100
                print(f"{self._name} just played {activity_choice} with you!")
                print(f"{self._name} is having a blast!\n")
                return

            print(f"{self._name} just played {activity_choice} with you!\n")

    @abc.abstractmethod
    def speak(self):
        pass


class Pikachu(Tamagotchi):

    def __init__(self, name="Pikachu", health=100, happiness=100, hunger=0):
        super().__init__(name, health, happiness, hunger)

        self.health_decay = 1.9
        self.hunger_decay = 2.5
        self.happiness_decay = 1.3

        self._favourite_food = "Blueberry"

    def speak(self):
        pikachu_lines = ["Pika pikaaaa", "Piakchuu", "Pika pika?", "Pikachuuuuuuu"]
        print(random.choice(pikachu_lines))


class Eevee(Tamagotchi):

    def __init__(self, name="Eevee", health=100, happiness=100, hunger=0):
        super().__init__(name, health, happiness, hunger)

        self.health_decay = 2.1
        self.hunger_decay = 1.9
        self.happiness_decay = 1.6

        self._favourite_food = "Strawberry"

    def speak(self):
        eevee_lines = ["Eevee!", "Eevee eevee eevee!", "Eeveee?", "Eevee eevee!"]
        print(random.choice(eevee_lines))


class Cyndaquil(Tamagotchi):

    def __init__(self, name="Cyndaquil", health=100, happiness=100, hunger=0):
        super().__init__(name, health, happiness, hunger)

        self.health_decay = 1.9
        self.hunger_decay = 1.5
        self.happiness_decay = 1.3

        self._favourite_food = "Mocha"

    def speak(self):
        cyndaquil_lines = ["Cynda!", "Cyndaquill!", "Cynda cyndaquil?", "Cyndaquill Cyndaquil!"]
        print(random.choice(cyndaquil_lines))


class Mew(Tamagotchi):

    def __init__(self, name="Mew", health=100, happiness=100, hunger=0):
        super().__init__(name, health, happiness, hunger)

        self.health_decay = 2.7
        self.hunger_decay = 1.5
        self.happiness_decay = .8

        self._favourite_food = "Coca-Cola"

    def speak(self):
        mew_lines = ["Mew?", "Mew mew!", "...?", "Meew!!!"]
        print(random.choice(mew_lines))


class Egg:

    def __init__(self):
        self.pokemon = [Cyndaquil, Pikachu, Mew, Eevee]

    def hatch(self):
        """
        Randomly hatches a Tamagotchi when it is called
        """
        random_pokemon = random.randint(0, len(self.pokemon) - 1)

        if random_pokemon == 0:
            return Cyndaquil()
        elif random_pokemon == 1:
            return Pikachu()
        elif random_pokemon == 2:
            return Mew()
        elif random_pokemon == 3:
            return Eevee()
