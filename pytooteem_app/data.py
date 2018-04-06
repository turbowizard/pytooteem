
# https://www.epicurious.com/recipes/food/views/3-ingredient-ice-cream-french-toast
recipe = (
    ('1', 'pint', 'vanilla ice cream (not gelato), melted'),
    ('4', '(1-1 0.5"-thick)', 'slices challah or brioche'),
    ('5', 'tablespoons', 'unsalted butter divided')
    )


class recipe_step:

    def __init__(self, a, v, c):
        self.amount, self.volume, self.content = a, v, c


def get_recipe_steps():
    return [recipe_step('1', 'pint', 'vanilla ice cream (not gelato), melted'),
            recipe_step('4', '(1-1 0.5"-thick)', 'slices challah or brioche'),
            recipe_step('5', 'tablespoons', 'unsalted butter divided')
            ]


