import pulp

# максимізація 
model = pulp.LpProblem("Maximize_Drinks_Production", pulp.LpMaximize)

# змінні
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# обмеження
water = 100
sugar = 50
lemon_juice = 30
fruit_puree = 40

# кількість ресурсів, необхідних для виробництва одиниці лимонаду
water_for_lemonade = 2
sugar_for_lemonade = 1
lemon_juice_for_lemonade = 1

# кількість ресурсів, необхідних для виробництва одиниці фруктового соку
water_for_fruit_juice = 1
fruit_puree_for_fruit_juice = 2

# максимізувати загальну кількість вироблених продуктів
model += lemonade + fruit_juice, "Total Drinks Produced"

# обмеження на ресурси
model += (water_for_lemonade * lemonade + water_for_fruit_juice * fruit_juice <= water), "Water Constraint"
model += (sugar_for_lemonade * lemonade <= sugar), "Sugar Constraint"
model += (lemon_juice_for_lemonade * lemonade <= lemon_juice), "Lemon Juice Constraint"
model += (fruit_puree_for_fruit_juice * fruit_juice <= fruit_puree), "Fruit Puree Constraint"

# пошук рішення
model.solve()

# результати
print(f"Статус моделі: {pulp.LpStatus[model.status]}")
print(f"Виробництво лимонаду: {pulp.value(lemonade)}")
print(f"Виробництво фруктового соку: {pulp.value(fruit_juice)}")
