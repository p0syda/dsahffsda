def get_cook_book(file_path):
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                ingredient_parts = ingredient_line.split('|')
                ingredient_dict = {
                    'ingredient_name': ingredient_parts[0].strip(),
                    'quantity': int(ingredient_parts[1].strip()),
                    'measure': ingredient_parts[2].strip()
                }
                ingredients.append(ingredient_dict)
            cook_book[dish_name] = ingredients
            # Пропускаем пустую строку
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

# Путь к локальному файлу с рецептами
file_path = 'recipes.txt'
cook_book = get_cook_book(file_path)

# Пример использования функции
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(shop_list)