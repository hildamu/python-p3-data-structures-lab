spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []  
    for food in spicy_foods:  
        names.append(food["name"])  
    return names  

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if isinstance(food, dict) and "heat_level" in food:
            if food["heat_level"] > 5:
                spiciest_foods.append(food)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level_emojis = "🌶" * food["heat_level"] 
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_spicy_foods = len(spicy_foods)
    
    if num_spicy_foods == 0:
        return 0  
    
    for food in spicy_foods:
        total_heat_level += food["heat_level"]

    return total_heat_level / num_spicy_foods

def create_spicy_food(spicy_foods, new_spicy_food):
    updated_spicy_foods = spicy_foods.copy()
    updated_spicy_foods.append(new_spicy_food)
    return updated_spicy_foods

