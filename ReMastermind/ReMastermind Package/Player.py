# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import random
class Player ():
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__ (self):
        self.inventory = []
        self.challenges = ["Determine the/Combination in/5 Guesses/or Less",
                           "Determine the/Combination in/7 Guesses/or Less",
                           "Determine the/Combination in/9 Guesses/or Less",
                           "Win 2 Games/in a Row",
                           "Win 3 Games/in a Row",
                           "Complete a Game/in 1 Minute/or less",
                           "Complete a Game/in 2 Minutes/or less",
                           "Complete a Game/in 3 Minutes/or less"]
        self.rewards = [300, 150, 50, 100, 200, 400, 250, 100]
        self.balance = 0
        self.selected_challenges = random.sample (self.challenges, 3)
        self.powerups = ["Reveal 1 character and its placement",
                         "Reveal 2 characters and their placements",
                         "Reveal 1 character without its placement",
                         "Reveal all 4 characters without their placements",
                         "Get an extra guess"]
        self.powerup_prices = [100, 175, 50, 300, 500]
        self.first_challenge = self.selected_challenges[0]
        self.second_challenge = self.selected_challenges[1]
        self.third_challenge = self.selected_challenges[2]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # Adds the purchased power-up to the user's inventory
    def add_inventory (self, challenge_num):
        self.inventory.append (self.powerups[challenge_num])
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # Adds balance to the user
    def add_balance (self, amount):
        self.balance += amount
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # Subtracts balance from the user
    def subtract_balance (self, amount):
        self.balance -= amount
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # Shows balance
    def show_balance (self):
        return self.balance
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
