
class Meal:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __repr__(self):
        nl = '\n    '
        return (f"{self.name}:{nl}"
           f"{nl.join([ingredient['amount'] + ' ' + ingredient['units'] + ' ' + ingredient['name'] for ingredient in self.ingredients])}")


class UnitConverter:
    dry_conversions = {
        "cup": 1,
        "oz": 8,
        "tbs": 16,
        "tsp": 48,
        "gram": 225,
    }
    liquid_conversions = {
        "pint": 0.5,
        "cup": 1,
        "oz": 8,
        "tbs": 16,
        "tsp": 48,
        "ml": 237,
    }

    def convert_unit(self, convert_from, convert_to, amount, liquid=False):
        if liquid is True:
            if convert_from in self.liquid_conversions:
                return float(self.liquid_conversions[convert_from]) / float(self.liquid_conversions[convert_to]) * float(amount)
            else:
                print(f"ERROR: {convert_from} not in liquid conversions")
                return 0
        else:
            if convert_from in self.dry_conversions:
                return float(self.dry_conversions[convert_from]) / float(self.dry_conversions[convert_to]) * float(amount)
            else:
                print(f"ERROR: {convert_from} not in dry conversions")
                return 0


class GroceryList:
    ingredients = {}
    unit_converter = UnitConverter()

    def __repr__(self):
        display_list = "Groceries:\n"
        nl = '\n'

        for key, ingredient in self.ingredients.items():
            display_list += f"  {ingredient['amount']} {ingredient['units']} {key + nl}"

        return display_list

    def add_meal(self, meal, count):
        for ingredient in meal.ingredients:
            key = ingredient['name']
            if key in self.ingredients:
                converted_amount = self.unit_converter.convert_unit(
                    ingredient['units'], 
                    self.ingredients[key]['units'], 
                    ingredient['amount']
                )
                self.ingredients[key]['amount'] += converted_amount * count
            else:
                self.ingredients[key] = {
                    'amount': float(ingredient['amount']) * count,
                    'units': ingredient['units']
                }
