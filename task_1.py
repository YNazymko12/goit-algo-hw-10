import pulp

# Створення моделі задачі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Об'єктивна функція (максимізація загальної кількості вироблених продуктів)
model += x1 + x2, "Total Products"

# Обмеження на ресурси
model += 2 * x1 + 1 * x2 <= 100, "Water"
model += 1 * x1 <= 50, "Sugar"
model += 1 * x1 <= 30, "LemonJuice"
model += 2 * x2 <= 40, "FruitPuree"

# Розв'язання задачі
model.solve()

# Виведення результатів
print("Status:", pulp.LpStatus[model.status])
print("Lemonade production:", pulp.value(x1))
print("Fruit Juice production:", pulp.value(x2))
print("Total products produced:", pulp.value(x1) + pulp.value(x2))