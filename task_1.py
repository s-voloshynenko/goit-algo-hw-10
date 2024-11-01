"""
1. "Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
2. "Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
3. Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
4. Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
5. Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".
Використовуючи PuLP, створіть модель, яка визначає, скільки "Лимонаду" та "Фруктового соку" потрібно виробити
для максимізації загальної кількості продуктів, дотримуючись обмежень на ресурси.
Напишіть програму, код якої максимізує загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік",
враховуючи обмеження на кількість ресурсів.
"""

import pulp

model = pulp.LpProblem("Maximize_Products", pulp.LpMaximize)

# variables
Lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
Fruit_Juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# max function
model += Lemonade + Fruit_Juice, "Total_Products"

# constraints
model += 2 * Lemonade + 1 * Fruit_Juice <= 100, "Water_Constraint"
model += 1 * Lemonade <= 50, "Sugar_Constraint"
model += 1 * Lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * Fruit_Juice <= 40, "Fruit_Puree_Constraint"

# solve
model.solve()

# results
lemonade_count = Lemonade.varValue
fruit_juice_count = Fruit_Juice.varValue

print("Results:")
print("Lemonade:", lemonade_count)
print("Fruit Juice:", fruit_juice_count)
print("Total:", lemonade_count + fruit_juice_count)
