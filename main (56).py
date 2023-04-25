import random

# Define the ingredients and their respective nutrient values in a dictionary
ingredients = {
    "Spinach": {"vitamin A": 56, "vitamin C": 14, "iron": 1},
    "Kale": {"vitamin A": 49, "vitamin C": 35, "iron": 1},
    "Carrots": {"vitamin A": 334, "vitamin C": 9, "iron": 0},
    "Mango": {"vitamin A": 1262, "vitamin C": 45, "iron": 1},
    "Banana": {"vitamin A": 64, "vitamin C": 10, "iron": 1},
    "Blueberries": {"vitamin A": 54, "vitamin C": 14, "iron": 1},
    "Almond Milk": {"vitamin A": 0, "vitamin C": 0, "iron": 2},
    "Greek Yogurt": {"vitamin A": 0, "vitamin C": 0, "iron": 1},
    "Chia Seeds": {"vitamin A": 0, "vitamin C": 0, "iron": 4}
}

# Define a list of days of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Define a function to select a random ingredient and its respective nutrient values
def select_ingredient():
    ingredient = random.choice(list(ingredients.keys()))
    return (ingredient, ingredients[ingredient])

# Generate a smoothie for each day of the week
for day in days_of_week:
    print(day + ":")
    # Select three random ingredients for each smoothie
    smoothie_ingredients = [select_ingredient(), select_ingredient(), select_ingredient()]
    # Calculate the total nutrient values for the smoothie
    total_vitamin_a = sum([ingredient[1]['vitamin A'] for ingredient in smoothie_ingredients])
    total_vitamin_c = sum([ingredient[1]['vitamin C'] for ingredient in smoothie_ingredients])
    total_iron = sum([ingredient[1]['iron'] for ingredient in smoothie_ingredients])
    # Print the smoothie ingredients and their respective nutrient values
    for ingredient in smoothie_ingredients:
        print("- " + ingredient[0] + ": " + str(ingredient[1]['vitamin A']) + " IU of vitamin A, " + str(ingredient[1]['vitamin C']) + " mg of vitamin C, and " + str(ingredient[1]['iron']) + " mg of iron")
    print("Total Nutrient Values: " + str(total_vitamin_a) + " IU of vitamin A, " + str(total_vitamin_c) + " mg of vitamin C, and " + str(total_iron) + " mg of iron")
    print("\n")
