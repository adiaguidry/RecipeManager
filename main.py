from pathlib import Path
from os import system

path = Path(Path.home() / 'Recipes')

#path to directory for recipe folder
def start_program():
    print(f'{"*" * 10} Welcome to the Recipe Admin {"*" * 10}')
    print(f'Path to the recipes: {Path(Path.home() / "Recipes")}')
    print('*' * 50 + '\n')


#how many recipes there are inside the folder
def count_recipes():
    count = 0
    all_recipes = path.glob('**/*.txt')
    for recipe in all_recipes:
        count+=1
        print(recipe)
    print(f'There are {count} recipes in our box')

#select an option
def select_option():
    option_dic = {
        '[1]': 'read recipe',
        '[2]': 'create recipe',
        '[3]': 'create category',
        '[4]': 'delete recipe',
        '[5]': 'end program'
    }
    for number, option in option_dic.items():
         print(f'\t{number}:{option}')
    option = input('\nWhich option would you like: ')
    match_option(option)


def handle_read():
    system('clear')
    category_dic = {}
    recipe_dic = {}
    count = 1
    for category in path.iterdir():
        if category.stem != '.DS_Store':
            category_dic[count] = category.name
            count+=1
    for key, value in category_dic.items():
        print(f'{key} : {value}')
    category = category_dic[int(input('Select a category: '))]
    system('clear')
    recipes = Path(Path.home() / 'Recipes' / category).glob('*.txt')
    for recipe in recipes:
        print(recipe.stem)
    recipe = input('Select a recipe to read: ') + '.txt'
    system('clear')
    selected_recipe = Path(Path.home() / 'Recipes' / category / recipe)
    print(Path.read_text(selected_recipe))
    select_option()


def handle_create_recipe():
    all_recipes = Path(Path.home() / 'Recipes').glob('**')
    for category in all_recipes:
        print(category.stem)
    category_type = input('Select a category to create a recipe for: ')
    system('clear')
    name = input('What is the name of your recipe: ')
    system('clear')
    category = Path(Path.home() / 'Recipes' / category_type)
    name = name + '.txt'
    file = Path(category / name)
    Path.touch(Path.home() / 'Recipes' / category_type / name)
    file.write_text(input('Enter your recipe here: '))
    system('clear')
    print('Thank you for the recipe')
    select_option()


def handle_create_category():
    category_type = input('Enter a category you would like to create: ')
    Path.mkdir(Path.home() / 'Recipes' / category_type)
    all_recipes = Path(Path.home() / 'Recipes' / category_type).glob('**')
    for category in all_recipes:
        print(category.stem)
    print('Thank you for adding a category to our recipe box')
    select_option()


def handle_delete_recipe():
    system('clear')
    recipe_file = Path(input('Enter recipe you would like to delete: ') + '.txt')
    path = Path(recipe_file).absolute()
    print(path)
    all_recipes = Path(Path.home() / 'Recipes').glob('**/*.txt')
    for category in all_recipes:
        print(category.stem)
    select_option()


def handle_delete_category():
    system('clear')
    category_file = Path(input('Enter category you would like to delete: ') + '.txt')
    path = Path(category_file).parents
    print(path)
    all_recipes = Path(Path.home() / 'Recipes').glob('**')
    for category in all_recipes:
        print(category.stem)
    select_option()


def match_option(option):
    match option:
        case '1':
            handle_read()
        case '2':
            handle_create_recipe()
        case '3':
            handle_delete_recipe()
        case '4':
            handle_delete_category()
        case _:
            print('select a option from the list')

start_program()
select_option()


