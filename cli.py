import json
from classes import Meal, GroceryList

class CLI:
    def __init__(self):
        self.meals = self.load_meals()
        print()
        print("Welcome to the grocery list generator")
        print()

        self.display_help()

        user_input = self.prompt().split()

        while (user_input[0] != "quit"):
            print()
            self.process_command(user_input)
            user_input = self.prompt().split()

    def prompt(self):
        return input("> ")
            
    def process_command(self, user_input):
        if user_input[0] == 'add_meal':
            self.add_meal(user_input)
        elif user_input[0] == 'list_meals':
            self.list_meals(user_input)
        elif user_input[0] == 'generate_list':
            self.generate_list()
        elif user_input[0] == 'help':
            self.display_help()
        else:
            print(f"ERROR: {user_input[0]} is not a supported command.")
            self.display_help()

    def display_help(self):
        print("usage: <command> <options>\n"
            "commands:\n"
            "   add_meal <meal_name> <[ingredients]>\n"
            "       ingredient format: <name>/<amount>/<units>\n"
            "   list_meals <options>\n"
            "       options:\n"
            "           -i: show ingredients\n"
            "   generate_list\n"
            "   help\n"
            "   quit\n")

    def load_meals(self):
        meals = []
        with open('meals.json', 'r') as f:
            data = json.load(f)
            for meal in data:
                meals.append(Meal(meal, data[meal]['ingredients']))
            
        return meals

    def add_meal(self, params):
        ingredients = []
        if len(params) > 2:
            for i in range(2, len(params)):
                ingredient = params[i].split('/')
                ingredients.append({
                    'name': ingredient[0],
                    'amount': ingredient[1],
                    'units': ingredient[2]
                })
        else:
            print("ERROR: ingredients must be included in command")
            self.display_help()
            return
        
        self.meals.append(Meal(params[1], ingredients))

        self.update_json()

    def update_json(self):
        new_json = {}
        for meal in self.meals:
            new_json[meal.name] = {"ingredients": meal.ingredients}
        with open('meals.json', 'w') as f:
            json.dump(new_json, f, indent=4)

    def list_meals(self, params):
        for meal in self.meals:
            if len(params) > 1 and params[1] == "-i":
                print(meal)
            else:
                print(meal.name)
        print()

    def generate_list(self):
        self.grocery_list = GroceryList()
        print("For each meal, enter the quantity you would like to make.")

        for meal in self.meals:
            quantity = float(input(meal.name + ": "))

            if quantity > 0:
                self.grocery_list.add_meal(meal, quantity)

        print()
        print(self.grocery_list)
