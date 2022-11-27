from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def calculate_recipes(request, recipe):

    if recipe in DATA:
        data = DATA[recipe]
        servings = request.GET.get('servings', None)

        if servings:
            result = dict()
            for item, value in data.items():
                new_value = value * int(servings)
                result[item] = new_value
            context = {
                'recipe_name': recipe,
                'recipe': result
            }
        else:
            context = {
                'recipe_name': recipe,
                'recipe': data
            }

    else:
        context = None

    return render(request, template_name='calculator/index.html', context=context)


def home(request):

    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}

    return render(request, template_name='home.html', context=context)